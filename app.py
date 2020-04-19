import requests
import os
from bs4 import BeautifulSoup
import shutil

url = ('https://www.bing.com/')

bing_t = requests.get(url)
beauty_bing = BeautifulSoup(bing_t.text, 'html.parser')

# print(beauty_bing.findAll(id='preloadBg'))
img_link = beauty_bing.findAll(id='preloadBg')
# img_src = img_link.href
# print(type(img_link))
# print(bing_t.text)

# images = []
for i in img_link:
    src = i['href']
    # images.append(src)

img_src = 'https://bing.com'+src

# print(img_src)
img_r = requests.get(img_src, stream=True)
with open('img.jpg',"wb") as output_file:
    shutil.copyfileobj(img_r.raw, output_file)

os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/ooyeraju/projects/wallpaper/img.jpg")

