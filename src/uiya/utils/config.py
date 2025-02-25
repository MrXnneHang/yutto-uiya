from __future__ import annotations

from pathlib import Path

import yaml
import os
import platform


def xdg_config_home() -> Path:
    if (env := os.environ.get("XDG_CONFIG_HOME")) and (path := Path(env)).is_absolute():
        return path
    home = Path.home()
    if platform.system() == "Windows":
        return home / "AppData"
    return home / ".config"


def search_for_settings_file() -> Path | None:
    settings_file = Path("yutto_uiya.yaml")
    if not settings_file.exists():
        settings_file = xdg_config_home() / "yutto_uiya.yaml"
    if not settings_file.exists():
        return None
    return settings_file


# 读取配置文件
def load_config() -> dict[str, bool | str]:
    """读取配置文件到字典"""
    path = search_for_settings_file()
    try:
        if path is None:
            print(
                """
请确保创建了配置文件yutto_uiya.yaml
可以创建在当前目录下,或者:
对于windows用户,创建在C:/User/你的用户名/.config/yutto.yaml,
对于非windows用户，创建在~/.config/yutto_uiya.yaml.

默认配置:

SESS_DATA: "" # SESSDATA,用来伪装登陆信息,需要更高分辨率或者下载大会员视频，则需要填写，并且需要开通大会员。
download_dir: "./downloads" # 下载后保存的路径
login_strict: true  # 仅当SESSDATA不为空时生效，严格校验登陆信息是否有效
                    # 如果SESSDATA填写错误，会导致校验失败。
vip_strict: false   # 仅当SESSDATA不为空时生效，严格校验大会员，
                    # 如果不是大会员，请设置false,否则会无法下载。
                    # 如果是大会员，请设置true,否则有时候会被当成普通用户拦截。

具体参见: https://github.com/MrXnneHang/yutto-uiya
"""
            )
            raise FileNotFoundError("配置文件不存在")
        else:
            with path.open(encoding="utf-8") as f:
                return yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        # 打印错误信息
        print(f"配置文件 {path} 不存在")
        return {}


def write_config(path: str, data: dict[str, bool | str]) -> None:
    """写入配置文件"""
    with Path(path).open("w", encoding="utf-8") as f:
        yaml.dump(data, f)
    print(f"配置文件 {path} 写入成功")
