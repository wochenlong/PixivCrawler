from config import DOWNLOAD_CONFIG
from crawlers.bookmark_crawler import BookmarkCrawler
from crawlers.keyword_crawler import KeywordCrawler
from crawlers.ranking_crawler import RankingCrawler
from crawlers.users_crawler import UserCrawler
from utils import checkDir


if __name__ == "__main__":
    checkDir(DOWNLOAD_CONFIG["STORE_PATH"])

    app = KeywordCrawler(
        keyword=" 1000users入り",
        order=True,
        mode=["safe"][-1],
        n_images=600000,
        capacity=9999999,
    )
    app.run()
