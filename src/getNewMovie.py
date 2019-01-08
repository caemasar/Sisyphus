import sys 
sys.path.append("..")

import os
import queue
import re
import component.idvLogger as iLogger
from urllib import request
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup


log = iLogger.Logger('../log/all.log',level='debug')

def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')

def printPro(massage):
    log.logger.info(massage)
    # print(massage)

# TODO 各个步骤需要分成函数
# TODO 数据需要写到数据库里去
# TODO redis 做已经更新不关注
if __name__ == '__main__':

    title_web = {} 
    re_try_time = 3
    reg_format_punctuation = "[\s+\.\!_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）:：]+"
    movie_web = "https://www.dytt8.net/"

    fail_time = 0

    new_movie_class = ".co_content2 a"
    care_movie_title_list_file_path = "../resource/careMovie.lis"

    new_movie_title_list = []
    care_movie_title_list = []
    tamp_fail_addr_queue = queue.Queue()

    care_movie_title_list_file = open(
        care_movie_title_list_file_path, 'r', encoding='UTF-8')

    sourceInLine = care_movie_title_list_file.readlines()

    for line in sourceInLine:
        temp1 = line.strip('\n')
        temp1 = temp1.replace('-', '')
        if not temp1.startswith("#"):
            care_movie_title_list.append(
                re.sub(reg_format_punctuation, "", temp1))
    printPro("----------------------------------")
    printPro("关注列表")
    printPro(care_movie_title_list)
    printPro("----------------------------------")
    printPro("")

    printPro("----------------------------------")
    printPro("爬取到的信息")

    index_doc = pq(movie_web)
    movie_hrefs = index_doc(new_movie_class)
    printPro("共取到"+str(len(movie_hrefs))+"条连接")
    for href_index in movie_hrefs:
        new_movie_addr = movie_hrefs(href_index).attr("href")
        if new_movie_addr is not None:
            new_movie_addr = movie_web + new_movie_addr
            # printPro(new_movie_addr)
            # TODO 设置超时和失败重读
            try:
                new_movie_web = request.urlopen(new_movie_addr, timeout=7)
                bsObj = BeautifulSoup(new_movie_web.read(), 'lxml')
                new_movie_title = bsObj.title.text

                # pq(new_movie_addr).find("title").text()
                printPro(new_movie_title)
                # printPro(type(new_movie_title))
                start_index = new_movie_title.find("《") + 1
                end_index = new_movie_title.find("》")
                # printPro(type(start_index))
                new_movie_title = new_movie_title[start_index:end_index]
                # TODO 成功数失败数重试次数限制，逗号处理
                # TODO 字符处理需要写一个函数
                new_movie_title = re.sub(
                    reg_format_punctuation, "", new_movie_title)
                new_movie_title_tamp = new_movie_title.split("/")
                for new_movie_title_tamp_index in new_movie_title_tamp:
                        title_web[new_movie_title_tamp_index] = new_movie_addr
                printPro(new_movie_title_tamp)
                new_movie_title_list += new_movie_title_tamp
            except:
                fail_time += 1
                tamp_fail_addr_queue.put(new_movie_addr)
    printPro("共更新"+str(len(new_movie_title_list))+"部（多个名字的算多部）")
    printPro("失败尝试"+str(fail_time)+"次")
    tamp_fail_addr_queue.put("")
    printPro("----------------------------------")
    printPro("")

    printPro("----------------------------------")
    printPro("已经更新的列表")
    printPro(new_movie_title_list)
    # printPro(title_web)
    printPro("----------------------------------")
    printPro("")

    printPro("----------------------------------")
    while not tamp_fail_addr_queue.empty():
        tamp_fail_addr = tamp_fail_addr_queue.get()
        try:
            if not tamp_fail_addr == "" and re_try_time > 0:
                new_movie_web2 = request.urlopen(tamp_fail_addr, timeout=7)
                bsObj2 = BeautifulSoup(new_movie_web2.read(), 'lxml')
                new_movie_title2 = bsObj2.title.text

                # pq(new_movie_addr).find("title").text()
                printPro(new_movie_title2)
                # printPro(type(new_movie_title))
                start_index = new_movie_title2.find("《") + 1
                end_index = new_movie_title2.find("》")
                # printPro(type(start_index))
                new_movie_title2 = new_movie_title2[start_index:end_index]
                new_movie_title2_tamp = new_movie_title2.split("/")
                printPro(new_movie_title2_tamp)
                new_movie_title_list += new_movie_title2_tamp
            else:
                re_try_time -= 1
        except:
            tamp_fail_addr_queue.put(tamp_fail_addr)

    printPro("完成重试")
    printPro("重试后的更新列表")
    printPro(new_movie_title_list)
    printPro("----------------------------------")
    printPro("")

    updated_movie = [
        val for val in new_movie_title_list if val in care_movie_title_list]
    printPro("----------------------------------")
    printPro("关注且更新的列表")
    printPro(updated_movie)
    printPro("----------------------------------")

    if not len(updated_movie) < 1:
        careResult = open(GetDesktopPath()+'/careResult.txt', 'w')
        for updated_movie_index in updated_movie:
            careResult.write(updated_movie_index)
            careResult.write(title_web.get(updated_movie_index,""))
        careResult.close()
