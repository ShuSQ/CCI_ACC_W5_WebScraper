
import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://www.bilibili.com")
soup = BeautifulSoup(page.content, 'html.parser')

all_videos = []
videos = soup.select('div.info-box')
for video in videos:
    title = video.select('div.info > p.title')[0].text.strip()
    up_name = video.select('p.up')[0].text.strip()
    play_num = video.select('p.play')[0].text.strip()
    cover_img = video.select('img')[0].get('src')

    all_videos.append({
        "title": title,
        "upName": up_name,
        "playNum": play_num,
        "coverImg": cover_img
    })

keys = all_videos[0].keys()

with open('videos.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_videos)