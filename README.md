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
│
└── __main__.py # 这个是我们的 webui 入口文件
│
└──  api.py # 封装好的各个交互事件
│
└──  _typing.py # 记录一些数据结构以及变量含义

```
## 如何部署它:

你需要`ffmpeg`，我正在研究如何为`windows`用户指定相对路径里的`ffmpeg`。或者在每次使用的时候`export`本地的`ffmpeg`到环境变量。<br>

对于`mac/linux`用户:<br>

```shell
brew install ffmpeg # mac
sudo apt install ffmpeg # linux
```

然后你可以直接从我的仓库安装。<br>

```shell
# python >=3.10
git clone https://github.com/MrXnneHang/yutto-uiya.git
# 用 uv 安装, 更快。
uv pip install git+https://github.com/MrXnneHang/yutto-uiya.git@gradio-webui
# 或者用 pip 安装
pip install git+https://github.com/MrXnneHang/yutto-uiya.git@gradio-webui
```

## 启动:<br>

```shell
(test-uiya) xnne@xnne-PC:~/code/test-uiya$ uiya
* Running on local URL:  http://127.0.0.1:7860

To create a public link, set `share=True` in `launch()`
```

## 关于配置文件:

`./yutto_uiya.yaml`

如果你保持在这个目录下使用，你可以直接修改这个文件。如果你希望在任何地方都可以使用，那么可以考虑把该文件复制到你的`USER_HOME/.config/`下方.有时候`.config`文件夹需要自己创建。<br>

对于 linux/mac 用户来说: `~/.config/yutto_uiya.yaml`

对于 windows 用户来说: `C:/User/Zhouyuan(你的用户名)/.config/yutto_uiya.yaml`

并且把考虑把`download_dir`改成绝对目录。<br>

```yaml
SESS_DATA: "" # SESSDATA,用来伪装登陆信息
download_dir: "./downloads" # 下载后保存的路径

# 这两个决定能下哪些视频，清晰度，用户有访问哪些视频的权限，就能下哪些视频，
# 比如大会员视频就需要大会员登陆的SESSDATA
# 而无登陆用户最高只能下载480p
login_strict: true # 仅当SESSDATA不为空时生效，严格校验登陆信息是否有效
                   # 如果SESSDATA填写错误，会导致校验失败。
vip_strict: false # 仅当SESSDATA不为空时生效，严格校验大会员，
                  # 如果不是大会员，请设置false,否则会无法下载。
                  # 如果是大会员，请设置true,否则有时候会被当成普通用户拦截。
```

SESSDATA是用来伪装登陆的，它会决定你的访问权限，如果需要下载更高分辨率或者对于需要大会员才能下载的资源则需要**获取SESSDATA**。<br>

具体方式参考[`./SESS_DATA/README.md`](https://github.com/MrXnneHang/yutto-uiya/tree/gradio-webui/SESS_DATA)<br>.



## 预览：
![image-20250220195748641](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/25/02/202502202049967.png)
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

### 如何用它下载视频:

我为每个功能都在`webui`中写了说明，放心食用~<br>

## 待开发:

- [x] 提供单独下载音频、视频、弹幕、封面的勾选项。放在webui中。 
- [ ] 结合 nfo 显示部分视频信息。
- [ ] 提供手动选集。 
- [x] Typing，优化代码结构，让代码变得优雅.    
- [x]  release as a python package
