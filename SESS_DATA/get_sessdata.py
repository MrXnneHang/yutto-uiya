from __future__ import annotations

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path

import yaml


# 读取配置文件
def load_config(path: str) -> dict[str, bool | str]:
    """读取配置文件到字典"""

    try:
        with Path(path).open(encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        # 打印错误信息
        print(f"配置文件 {path} 不存在")
        return {}


class ChromeDriverConfig:
    def __init__(self):
        self.args: dict[str, str] = load_config("./configs/chrome.yaml")
        self.option = webdriver.ChromeOptions()
        self.option.add_argument(r"user-data-dir=./User Data")  # 浏览器路径

        # 指定Chrome和ChromeDriver的路径
        self.chrome_path = self.args["chrome"]
        self.chrome_driver_path = self.args["chrome_driver"]
        self.option.binary_location = self.chrome_path

        # 使用Service指定ChromeDriver的路径
        self.service = Service(self.chrome_driver_path)


if __name__ == "__main__":
    chrome_config = ChromeDriverConfig()
    # 初始化driver
    driver = webdriver.Chrome(
        service=chrome_config.service, options=chrome_config.option
    )
    driver.get(chrome_config.args["target_url"])
    sleep(3)
    # 获取 cookies
    cookies = driver.get_cookies()

    # 查找 SESSDATA cookie
    sessdata = ""
    for cookie in cookies:
        if cookie["name"] == "SESSDATA":
            sessdata = cookie["value"]
            print(cookie["name"] + ": ", sessdata)

    if sessdata:
        print(
            "复制你的SESSDATA，然后填写到./configs/args.yaml的SESSDATA中,写在双引号中"
        )
    else:
        print("第一次打开浏览器，需要先登陆bilibili账号，然后关闭窗口再次运行程序")

    sleep(100000)
