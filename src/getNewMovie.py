from pyquery import PyQuery as pq
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


movie_web = "https://www.dytt8.net/"

new_movie_class = ".co_content2 a"
care_movie_title_list_file_path = "../resource/careMovie"


new_movie_title_list = []
care_movie_title_list = []

care_movie_title_list_file = open(
    care_movie_title_list_file_path, 'r', encoding='UTF-8')

sourceInLine = care_movie_title_list_file.readlines()

for line in sourceInLine:
    temp1 = line.strip('\n')
    temp1 = temp1.replace('-', '')
    if not temp1.startswith("#"):
        care_movie_title_list.append(temp1)
print(care_movie_title_list)

index_doc = pq(movie_web)
movie_hrefs = index_doc(new_movie_class)
for href_index in movie_hrefs:
    new_movie_addr = movie_hrefs(href_index).attr("href")
    if new_movie_addr is not None:
        new_movie_addr = movie_web + new_movie_addr
        # print(new_movie_addr)
        # TODO 设置超时和失败重读
        new_movie_web = urlopen(new_movie_addr)
        bsObj = BeautifulSoup(new_movie_web.read(), 'lxml')
        new_movie_title = bsObj.title.text

        # pq(new_movie_addr).find("title").text()
        print(new_movie_title)
        # print(type(new_movie_title))
        start_index = new_movie_title.find("《") + 1
        end_index = new_movie_title.find("》")
        # print(type(start_index))
        new_movie_title = new_movie_title[start_index:end_index]
        new_movie_title_tamp = new_movie_title.split("/")
        print(new_movie_title_tamp)
        new_movie_title_list += new_movie_title_tamp
print(new_movie_title_list)
updated_movie = [
    val for val in new_movie_title_list if val in care_movie_title_list]

print(updated_movie)

if not len(updated_movie) < 1:
    careResult = open(GetDesktopPath()+'/careResult.txt', 'w')
    for updated_movie_index in updated_movie:
        careResult.write(updated_movie_index)
    careResult.close()
