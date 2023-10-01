import concurrent.futures as futures
from typing import Iterable, Set

from config import DOWNLOAD_CONFIG
from tqdm import tqdm
from utils import printInfo

from .download_image import downloadImage


class Downloader:
    """
    下载控制器
    """

    def __init__(self, capacity):
        self.url_group: Set[str] = set()  # 存储要下载的图片 URL 集合
        self.capacity = capacity

    def add(self, urls: Iterable[str]):
        """
        添加要下载的图片 URL
        """
        for url in urls:
            self.url_group.add(url)

    def download(self):
        """
        执行下载操作
        """
        flow_size = 0.0  # 记录下载的流量大小
        printInfo("===== 下载开始 =====")

        n_thread = DOWNLOAD_CONFIG["N_THREAD"]  # 并发下载线程数
        with futures.ThreadPoolExecutor(n_thread) as executor:
            with tqdm(total=len(self.url_group), desc="正在下载") as pbar:
                for image_size in executor.map(downloadImage, self.url_group):
                    flow_size += image_size
                    pbar.update()
                    pbar.set_description(f"正在下载 / 流量 {flow_size:.2f}MB")
                    if flow_size > self.capacity:
                        executor.shutdown(wait=False, cancel_futures=True)
                        break

        printInfo("===== 下载完成 =====")
        return flow_size
