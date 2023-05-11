import re
import os
import json
import requests

def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


def SaveFile(data, file_name, dir_path):
    tip = file_name.split('.')[0]
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    with open(dir_path + '\\' + file_name, mode='wb') as f:
        f.write(data)
    print(tip + 'Save Successfully！')


def Parse(html_text):
    try:
        string_re = re.findall('window.__playinfo__=(.*?)</script>', html_text)[0]
        json_data = json.loads(string_re)
        audio = json_data['data']['dash']['audio'][0]['backupUrl'][0]
        video = json_data['data']['dash']['video'][0]['backupUrl'][0]
        return video, audio
    except Exception as e:
        print('Error While Parsing:', e)
        return []


def GetSource(url, referer=None, proxy=None):
    headers = {'Referer': referer,
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
               }
    try:
        response = requests.get(url=url, headers=headers, proxies=proxy)
        return response
    except Exception as e:
        print('Error: ', e)
        return None