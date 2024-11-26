from __future__ import annotations

import json
from time import sleep
from pathlib import Path

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.config import load_config, write_config


class Wish(object):
    def __init__(self):
        self.config = load_config("./configs/chrome.yaml")
        self.option = webdriver.ChromeOptions()
        # 指定Chrome和ChromeDriver的路径
        self.chrome_path = self.config["chrome"]
        self.chrome_driver_path = self.config["chrome_driver"]
        self.option.binary_location = self.chrome_path
        # 获取用户数据目录的绝对路径
        script_dir = Path(__file__).resolve().parent
        self.user_data_dir = script_dir / 'User Data'


        self.option.add_argument(rf"user-data-dir={str(self.user_data_dir)}")  # 浏览器路径




        # 使用Service指定ChromeDriver的路径
        self.service = Service(self.chrome_driver_path)

    def get_data(self):
        """初始化WebDriver并获取cookies"""
        option = webdriver.ChromeOptions()
        option.add_argument(rf"user-data-dir={str(self.user_data_dir)}")  # 浏览器路径

        # 指定Chrome和ChromeDriver的路径
        chrome_path = self.config["chrome"]
        chrome_driver_path = self.config["chrome_driver"]
        option.binary_location = chrome_path

        # 使用Service指定ChromeDriver的路径
        service = Service(chrome_driver_path)

        # 初始化driver
        driver = webdriver.Chrome(service=service, options=option)
        driver.get(self.config["target_url"])
        sleep(5)  # 等待页面加载

    def run(self):
        self.get_data()


if __name__ == "__main__":
    fps = Wish()
    # 初始化driver
    driver = webdriver.Chrome(service=fps.service, options=fps.option)
    driver.get(fps.config["target_url"])
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
        print("可以关闭该窗口了....")
    else:
        print("第一次打开浏览器，需要先登录bilibili账号，然后再次运行程序")
        print("登录后就可以关闭该窗口了")

    sleep(100000)
