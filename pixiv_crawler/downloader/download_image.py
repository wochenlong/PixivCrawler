import os
import re
import time

import requests
from config import DOWNLOAD_CONFIG, NETWORK_CONFIG, OUTPUT_CONFIG
from utils import printError, printInfo, printWarn, writeFailLog


def downloadImage(url: str) -> float:
    """
    下载图片

    返回：图片大小（MB）

    注意：url 示例 "https://i.pximg.net/
        img-original/img/2022/05/11/00/00/12/98259515_p0.jpg"
    """

    image_name = url[url.rfind("/") + 1 :]  # 提取图片文件名
    result = re.search("/(\d+)_", url)  # 从 URL 中提取图片 ID
    printError(result is None, "图片下载器中的 URL 有误")
    image_id = result.group(1)
    headers = {"Referer": f"https://www.pixiv.net/artworks/{image_id}"}
    headers.update(NETWORK_CONFIG["HEADER"])

    verbose_output = OUTPUT_CONFIG["VERBOSE"]
    error_output = OUTPUT_CONFIG["PRINT_ERROR"]
    if verbose_output:
        printInfo(f"正在下载 {image_name}")
    time.sleep(DOWNLOAD_CONFIG["THREAD_DELAY"])

    image_path = DOWNLOAD_CONFIG["STORE_PATH"] + image_name
    if os.path.exists(image_path):
        printWarn(verbose_output, f"{image_path} 已存在")
        return 0

    wait_time = 10
    for i in range(DOWNLOAD_CONFIG["N_TIMES"]):
        try:
            response = requests.get(
                url,
                headers=headers,
                proxies=NETWORK_CONFIG["PROXY"],
                timeout=(4, wait_time),
            )

            if response.status_code == 200:
                image_size = int(response.headers["content-length"])
                # 删除不完整的图片
                if len(response.content) != image_size:
                    time.sleep(DOWNLOAD_CONFIG["FAIL_DELAY"])
                    wait_time += 2
                    continue

                with open(image_path, "wb") as f:
                    f.write(response.content)
                if verbose_output:
                    printInfo(f"{image_name} 下载完成")
                return image_size / (1 << 20)

        except Exception as e:
            printWarn(error_output, e)
            printWarn(error_output, f"这是第 {i} 次尝试下载 {image_name}")

            time.sleep(DOWNLOAD_CONFIG["FAIL_DELAY"])

    printWarn(error_output, f"无法下载 {image_name}")
    writeFailLog(f"无法下载 {image_name} \n")
    return 0
