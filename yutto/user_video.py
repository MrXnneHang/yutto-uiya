from __future__ import annotations

from utils.subproc import run_command


def user_single_video(url: str, args: list, SESSDATA: str = None) -> int:
    """
    下载单个视频
    :param url: 视频链接
    :param args: 额外输入参数
    :param SESSDATA: SESSDATA, 用于保持用户登录信息
    :return: 200/404/500
    """
    command = ["yutto", url]
    if SESSDATA:
        command.extend(["--sessdata", SESSDATA])
    if args:
        command.extend(args)  # 以空格分割额外参数

    try:
        run_command(command)
    except Exception as e:
        return 404
    return 200
