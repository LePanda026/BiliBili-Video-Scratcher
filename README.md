# B站音频爬虫
## 介绍
你可以通过输入BV号来获取B站视频的音频
## 步骤
### Python开发环境
确保您的电脑中有Python，且Python>=3.8
### 安装依赖
你需要安装以下依赖：<br />
re<br />
os<br />
json<br />
requests<br />
步骤：<br />
1、win+r打开cmd窗口<br />
2、输入：pip install re,os,json,requests
### BV号获取
1、手机端 <br />
打开客户端，视频下方 <br />
2、电脑端 <br />
打开视频，查看浏览器上方网址：
https://www.bilibili.com/video/<strong>BV1gr4y1X7JR</strong>/?spm_id_from=333.999.0.0&vd_source=cf6cf9610f172f80dfab4b63068094c6
### 运行
<strong>如果您是初学者，不具备开发环境（Pycharm/Jupyter Notebook/Spyder等）</strong><br />
1、win+r打开cmd窗口<br />
2、输入python+getAudio文件的路径(路径可以右键文件，点击安全即可查看）<br />
&emsp;例如：python P:\Python\project\ScratchBiliBili\getAudio.py<br />
3、分别输入您的BV号和您希望的音频名字即可
<strong>如果您不是，可以使用集成开发环境打开上述两个文件（Jupyter Notebook不支持）
1、您可以按需修改存放位置<br />
![image](https://github.com/LePanda026/BiliBili-Video-Scratcher/assets/106538913/60404ea9-7bad-46a4-9426-0024bf95be8d) <br />
2、运行即可
