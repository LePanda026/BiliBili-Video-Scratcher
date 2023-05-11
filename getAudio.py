from util import *

AUDIO_SAVE_DIC = r''
url = fr'https://www.bilibili.com/video/{input("Please Tell Me The BVID>>")}\
        /?spm_id_from=333.337.search-card.all.click&vd_source=cf6cf9610f172f80dfab4b63068094c6'

response = GetSource(url=url, proxy=None)
if str(response) == '<Response [200]>':
    html_text = response.text
    va_url = Parse(html_text)
    if va_url:
        audio_url = va_url[1]
        try:
            print('Downloading...')
            audio = GetSource(audio_url, url, None).content
            Find = True
            print('Download Successfully')
            SaveFile(audio, input('Please Tell Me The Audio Name That You Want>>') + '.mp3', AUDIO_SAVE_DIC)
        except Exception as e:
            print('Error While Downloading: ', e)