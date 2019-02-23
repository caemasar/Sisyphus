# 读取本地文件的一个尝试

import os
import re

if __name__ == '__main__':

    list_file_path = "../../resource/baidupan.lis"

    list_file = open(list_file_path, 'r', encoding='UTF-8')

    sourceInLine = list_file.readlines()
    for line in sourceInLine:
        tamp1 = line.strip('\n')
        # temp1.find("：")
        # temp1 = temp1.replace('-', '')
        # if not temp1.startswith("#"):
        # care_movie_title_list.append(
        #     re.sub(reg_format_punctuation, "", temp1))
        # print(temp1)
        # temp1List = temp1.split("链接")
        # tamp2 = ""
        # if len(temp1List) > 1:
        #     tamp2 = temp1List[1]
        # else:
        # temp2 = re.match(/^(http://){0,1}[A-Za-z0-9][A-Za-z0-9\-\.]+[A-Za-z0-9]\.[A-Za-z]{2,}[\43-\176]*$/,temp1)
        tamp2 = re.findall(r'(https?://\S+)',tamp1)
        if tamp2:
            # print(tamp1)
            # print(len(tamp2[0]))
            print(tamp1[tamp1.find(tamp2[0]):(tamp1.find(tamp2[0])+len(tamp2[0]))])
            # print(tamp1[tamp1.find(tamp2[0]):])
            print(tamp1[(tamp1.find(tamp2[0])+len(tamp2[0])):])
            

