import concurrent.futures as futures
from typing import Set

from collector.collector import Collector
from collector.collector_unit import collect
from collector.selectors import selectKeyword
from config import DOWNLOAD_CONFIG, USER_CONFIG
from config import DOWNLOAD_CONFIG, MODE_CONFIG, USER_CONFIG
from downloader.downloader import Downloader
from tqdm import tqdm
from utils import printInfo
import urllib.parse as urlparse


class KeywordCrawler:
    """关键字爬虫类
    下载特定关键字的搜索结果
    """

    def __init__(
        self,
        keyword: str,
        order: bool = False,
        mode: str = "safe",
        n_images=200,
        capacity=1024,
    ):
        assert mode in ["safe", "r18", "all"]

        self.keyword = keyword  # 关键字
        self.order = order  # 排序方式（是否按热度排序）
        self.mode = mode  # 模式（安全模式、R18模式或所有模式）

        self.n_images = n_images  # 下载的图片数量

        self.downloader = Downloader(capacity)  # 图片下载器
        self.collector = Collector(self.downloader)  # 数据收集器

    def collect(self):
        """从关键字搜索结果中收集插画的ID
        URL示例: "https://www.pixiv.net/ajax/search/artworks/{xxxxx}?
            word={xxxxx}&order=popular_d&mode=all&p=1&s_mode=s_tag_full&type=all&lang=zh"
        """

        # 每个关键字.json文件包含60个作品
        ARTWORK_PER = 60
        n_page = (self.n_images - 1) // ARTWORK_PER + 1  # 计算页数（上取整）
        printInfo(f"===== 开始收集关键字 {self.keyword} 的数据 =====")

        urls: Set[str] = set()
        url = (
            "https://www.pixiv.net/ajax/search/artworks/"
            + "{}?word={}".format(
                urlparse.quote(self.keyword, safe="()"), urlparse.quote(self.keyword)
            )
            + "&order={}".format("popular_d" if self.order else "date_d")
            + f"&mode={self.mode}"
            + "&p={}&s_mode=s_tag&type=all&lang=zh"
        )
        for i in range(n_page):
            urls.add(url.format(i + 1))

        n_thread = DOWNLOAD_CONFIG["N_THREAD"]
        with futures.ThreadPoolExecutor(n_thread) as executor:
            with tqdm(total=len(urls), desc="正在收集插画ID") as pbar:
                additional_headers = {"COOKIE": USER_CONFIG["COOKIE"]}
                for image_ids in executor.map(
                    collect,
                    zip(
                        urls,
                        [selectKeyword] * len(urls),
                        [additional_headers] * len(urls),
                    ),
                ):
                    if image_ids is not None:
                        self.collector.add(image_ids)
                    pbar.update()

        printInfo(f"===== 关键字 {self.keyword} 的数据收集完成 =====")
        printInfo(f"可下载的插画数量: {len(self.collector.id_group)}")

    def run(self):
        """运行关键字爬虫，包括收集插画ID和下载插画"""
        self.collect()
        self.collector.collect()
        return self.downloader.download()
