# yutto-uiya

<p align="center">
   <a href="https://python.org/" target="_blank"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/moelib?logo=python&style=flat-square"></a>
   <a href="https://pypi.org/project/moelib/" target="_blank"><img src="https://img.shields.io/pypi/v/moelib?style=flat-square" alt="pypi"></a>
    <a href="https://gradio.app/" target="_blank"><img alt="Gradio" src="https://img.shields.io/badge/Gradio-%20%F0%9F%92%BB-blue?style=flat-square"></a>
   <br/>
   <a href="https://github.com/astral-sh/uv"><img alt="uv" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&style=flat-square"></a>
   <a href="https://github.com/astral-sh/ruff"><img alt="ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square"></a>
   <a href="https://gitmoji.dev"><img alt="Gitmoji" src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67?style=flat-square"></a>
   <br/>
</p>

这里是 yutto 的 gradio-webui!<br>

原仓库:[https://github.com/yutto-dev/yutto](https://github.com/yutto-dev/yutto).<br>

## 为什么开发 ?​

我先前用过 downkyi,JJdown.共同的问题就是,我自己没能力改源代码。downkyi 是`C#`开发的，而 JJdown 似乎是闭源的。每次 b 站上的朋友问我说"为啥子突然不行了"，我也只能说我去向作者反馈一下，然后去提一个 Issue。<br>

但对于 yutto,我觉得我行了。<br>

## 暂定的目录结构:

```css
src/yutto-uiya/
│
├── yutto/ # 把yutto shell指令使用python调用，形成最小模块
│   └── __init__.py
│
├── utils/ # 这里是我们的工具包,只依赖于python标准库，以及一些第三方库，不依赖我们自己写的代码
│
├── configs/ # ffmpeg 等等配置文件我们会尝试放在这里.
│ └──  args.yaml # 和 yutto 相关的配置。 
└── __main__.py # 这个是我们的 webui 入口文件
└──  api.py # 封装好的各个交互事件
└──  _typing.py # 记录一些数据结构以及变量含义

```
## 如何部署它:

你需要`ffmpeg`，我正在研究如何为`windows`用户指定相对路径里的`ffmpeg`。或者在每次使用的时候`export`本地的`ffmpeg`到环境变量。<br>

对于`mac/linux`用户:<br>

```shell
brew install ffmpeg # mac
sudo apt install ffmpeg # linux
```

然后配置`python`环境:<br>

```shell
# python >=3.9
git clone https://github.com/MrXnneHang/yutto-uiya.git
cd yutto-uiya/
pip install pip install git+https://github.com/MrXnneHang/yutto.git@depndency-adjust # 因为 yutto 2.0.1 在 aiofiles 的依赖上和 gradio 有冲突，但又没有代码冲突，所以我手动调整了一下依赖版本
pip install -r requirements.txt
```

## 启动:<br>

```shell
cd src/yutto-uiya
python __main__.py
```
## 预览：
![image-20250220195748641](/home/xnne/.config/Typora/typora-user-images/image-20250220195748641.png)
![alt text](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/11/202411271939914.png)

## 一些配置:

参见[`./configs/`](https://github.com/MrXnneHang/yutto-uiya/tree/gradio-webui/configs):<br>

- `args.yaml`:
```yaml
SESSDATA: "" # SESSDATA,用来伪装登陆信息
download_dir: "./downloads" # 下载后保存的路径

no_danmaku: true # 不下载弹幕。

# 这两个决定能下哪些视频，清晰度，用户有访问哪些视频的权限，就能下哪些视频，
# 比如大会员视频就需要大会员登陆的SESSDATA
# 而无登陆用户最高只能下载480p
login_strict: true # 仅当SESSDATA不为空时生效，严格校验登陆信息是否有效
                   # 如果SESSDATA填写错误，会导致校验失败。
vip_strict: false # 仅当SESSDATA不为空时生效，严格校验大会员，
                  # 如果不是大会员，请设置false,否则会无法下载。
                  # 如果是大会员，请设置true,否则有时候会被当成普通用户拦截。

```

## 如何使用:

### 下载更高的清晰度或者大会员视频(你需要SESSDATA)

`sess_data`的获取:<br>

![image-20250220200623220](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/25/02/202502202006049.png)

你可以参考 [yutto 文档](https://yutto.nyakku.moe/guide/cli/basic)中提到的方法进行获取。或者使用我的脚本。<br>

你可以先下载`chrome-driver`和`chrome`然后根据你的路径配置`./configs/chrome.yaml`，然后运行:<br>

`chrome.yaml`: 配置`chrome-driver`来获取`sess_data`,如果你可以手动获取`sess_data`，那么这个文件可以不用配置。<br>

```yaml
chrome_driver: './chromedriver-linux64/chromedriver' # chrome-driver 路径
chrome: './chrome-linux64/chrome' # chrome 路径

# 如果你还没有使用过它们，你可以到这里下载你系统对应的版本:
# https://googlechromelabs.github.io/chrome-for-testing/#stable
# 然后解压，指定正确路径即可

target_url: 'https://www.bilibili.com/'
```


```shell
python webrowser_config.py
```

第一次打开后需要在打开的`chrome`页面中登陆你的`bilibili`账号，然后关闭页面，再次运行可以得到SESS_DATA。在终端中找到你的`SESSDATA`然后写入到`args.yaml`中。<br>

不过看起来似乎更麻烦？<br>

我会在做整合包的时候利用整合包环境直接 sh 或者 bat 脚本。<br>

### 如何用它下载视频:

我为每个功能都在`webui`中写了说明，放心食用~<br>

## 待开发:

- [x] 提供单独下载音频、视频、弹幕、封面的勾选项。放在webui中。
- [ ] 结合 nfo 显示部分视频信息。
- [ ] 提供手动选集。 
- [x] Typing，优化代码结构，让代码变得优雅.   
