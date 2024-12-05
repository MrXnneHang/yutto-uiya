from __future__ import annotations

from utils.subproc import run_command


# TODO: 似乎只支持-b,并且并不能直接获取url对应的那一话
# 下载单个番剧的指定一集
# 示例: https://www.bilibili.com/bangumi/play/ss48811
def bangumi_single_episode(url: str, args: list[str] = None) -> int:
    """
    下载单个番剧的指定一集
    :param url: 指定集数的番剧链接
    :param args: 额外输入参数
    :param SESSDATA: SESSDATA, 用于保持用户登录信息,如果下载大会员必须指定SESSDATA
    :return: 200/404/500
    """
    command = ["yutto", url, "-b"]

    if args:
        command.extend(args)

    try:
        run_command(command)
    except Exception as e:
        return 404
    return 200


# 下载单个番剧的指定一季
# 需要进入番剧主页,支持选集。
# 示例: https://www.bilibili.com/bangumi/media/md23053814
def bangumi_single_season(url: str, p: str = "", args: list = None):
    """
    下载单个番剧的指定一季
    :param url: 指定季数的番剧链接
    :param p: 指定要下载哪些p("1,2","1~2",start 1, end -1)
    :param args: 额外输入参数
    :param SESSDATA: SESSDATA, 用于保持用户登录信息,如果下载大会员必须指定SESSDATA
    :return: 200/404/500
    """
    if p:
        command = ["yutto", url, "-p", p, "-b"]
    else:
        # 全部下载
        command = ["yutto", url, "-p", "1~-1", "-b"]

    if args:
        command.extend(args)

    try:
        run_command(command)
    except Exception as e:
        return 404
    return 200
