from __future__ import annotations

import os
from pathlib import Path

import yaml

# 读取配置文件


def load_config(path: str) -> dict:
    """读取配置文件到字典"""

    try:
        with Path(path).open(encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        # 打印错误信息
        print(f"配置文件 {path} 不存在")
        return {}


def generate_args() -> str:
    """生成命令行参数"""
    config = load_config("./configs/args.yaml")
    args = ["-d", config["download_dir"]]

    return args
