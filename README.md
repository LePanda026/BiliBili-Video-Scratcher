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
3、分别输入您的BV号和您希望的音频名字即可<br />
<strong>如果您不是，可以使用集成开发环境打开上述两个文件（Jupyter Notebook不支持）</strong><br />
1、您可以按需修改存放位置<br />
![image](https://github.com/LePanda026/BiliBili-Video-Scratcher/assets/106538913/60404ea9-7bad-46a4-9426-0024bf95be8d) <br />
2、运行即可<br />
<strong>如果您有任何问题，请在issue中提交，或者微信联系我</strong>

# Bilibili Audio Crawler
## Introduction
You can use this program to obtain the audio of a Bilibili video by entering its BV number.

## Steps
### Python Development Environment
Make sure you have Python installed on your computer, and that it is at least version 3.8.

### Install Dependencies
You will need to install the following dependencies:<br />
re<br />
os<br />
json<br />
requests<br />
Steps:<br />
Press Win+R to open the command prompt.
Enter: pip install re,os,json,requests.

### Obtaining the BV Number
On a mobile device:<br />
Open the Bilibili app and find the video. The BV number is located at the bottom of the screen.
On a computer:<br />
Open the video and look at the URL in the browser:<br />
https://www.bilibili.com/video/<strong>BV1gr4y1X7JR</strong>/?spm_id_from=333.999.0.0&vd_source=cf6cf9610f172f80dfab4b63068094c6
### Running the Program
<strong>If you are a beginner and do not have a development environment (PyCharm/Jupyter Notebook/Spyder, etc.):</strong><br />

Press Win+R to open the command prompt.
Enter the path to the getAudio.py file using Python (you can right-click the file and click Properties to see the path).<br />
For example: python P:\Python\project\ScratchBiliBili\getAudio.py
Enter your BV number and the desired audio name.
<strong>If you are not a beginner, you can use an integrated development environment to open the above two files (Jupyter Notebook is not supported):</strong><br />

You can modify the storage location as needed.<br />
image
Run the program.<br />
<strong>If you have any questions, please submit them in the issues section or contact me via WeChat.</strong>
