# 你需要下载：

chromedriver 以及 chrome:

[https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)<br>

并且配置`./configs/chrome.yaml`中的`path` 为你的实际路径。<br>

之后 pip install -r requirements.txt。<br>

是的，目前这个脚本的环境和实际使用的环境是分开的，但后续会考虑用到 chromedriver 的 headless 模式来做一些事情，不然可以操作的就太少了。<br>

