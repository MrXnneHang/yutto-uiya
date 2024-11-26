from __future__ import annotations

import hashlib
import json
import re
import socket
import time
from datetime import datetime, timedelta
from hashlib import sha1
from time import sleep

import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.config import load_config


class Wish:
    def __init__(self):
        self.config = load_config("./configs/chrome.yaml")
        self.option = webdriver.ChromeOptions()
        self.option.add_argument(r"user-data-dir=./User Data")  # 浏览器路径

        # 指定Chrome和ChromeDriver的路径
        self.chrome_path = self.config["chrome"]
        self.chrome_driver_path = self.config["chrome_driver"]
        self.option.binary_location = self.chrome_path

        # 使用Service指定ChromeDriver的路径
        self.service = Service(self.chrome_driver_path)

    def get_data(self):
        """初始化WebDriver并获取cookies"""
        option = webdriver.ChromeOptions()
        option.add_argument(r"./User Data")  # 浏览器路径

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
    sleep(10000)
