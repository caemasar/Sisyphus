import webbrowser

webList = ["https://blog.csdn.net/lunzi3775/article/details/80387173",
"https://github.com/gawel/pyquery",
"https://pyquery.readthedocs.io/en/latest/",
"https://www.cnblogs.com/lei0213/p/7676254.html",
"https://www.cnblogs.com/zhaof/p/6935473.html",
"https://pypi.org/project/pyquery/",
"https://www.cnblogs.com/hdk1993/p/8010977.html",
"https://www.aliyun.com/jiaocheng/510734.html",
"https://www.cnblogs.com/jiu0821/p/6105890.html",
"https://blog.csdn.net/jin17864215570/article/details/82707985",
"https://www.cnblogs.com/nancyzhu/p/8449545.html",
"https://www.baidu.com/s?wd=Requirement%20already%20satisfied%3A&rsv_spt=1&rsv_iqid=0x97a1f586000ba336&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_n=2&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&inputT=210&rsv_sug4=210",
"https://www.baidu.com/s?wd=pyquery%20python%203.6&rsv_spt=1&rsv_iqid=0x90cd1eea000a85ec&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=pyquery%2520%25E5%25AE%2589%25E8%25A3%2585&inputT=4928&rsv_t=597eRoMrx3y6JhZCd9983T6Lwy9Kp%2Fy%2FK4kbc6vV6oA2jn1WYvGGBMtQXsbGl8yC4pQf&rsv_pq=e64f46a00001f93e&rsv_sug3=22&rsv_sug1=13&rsv_sug7=100&rsv_sug2=0&rsv_sug4=6795",
"https://blog.csdn.net/XK77167315/article/details/79904293",
"https://www.baidu.com/s?wd=python%20%E6%8F%92%E4%BB%B6%20list&rsv_spt=1&rsv_iqid=0xa8a7fb9c0001c3d0&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=python%2520%25E6%258F%2592%25E4%25BB%25B6&rsv_t=50cbHNjKKMHC2DZBsyQEKrKm9z%2BQ7GPg0Uxtffa0flLGrYRrXBSJ0hZJNJ3KINx30qU1&inputT=1021&rsv_pq=f629d632000174e2&rsv_sug3=20&rsv_sug1=11&rsv_sug7=100&rsv_sug2=0&rsv_sug4=2977",
"https://www.cnblogs.com/my1e3/p/6622306.html",
"https://www.baidu.com/s?wd=python%20%E7%BD%91%E9%A1%B5%E8%A7%A3%E6%9E%90&rsv_spt=1&rsv_iqid=0xe5dcdd6900016e68&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&prefixsug=python%2520%25E7%25BD%2591%25E9%25A1%25B5&rsp=1&inputT=8361&rsv_sug4=8361",
"https://www.baidu.com/s?wd=python%20%E8%B0%83%E7%94%A8python&rsv_spt=1&rsv_iqid=0xb5c031d60009f0c2&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=python%2520%25E8%25B0%2583%25E7%2594%25A8exe&inputT=1727&rsv_t=d7a1OfJyJ%2F3dVYzyRjQyAbV4yT4OlKofHLiwRXf%2FC7i%2FRRFdwv%2F8u3J7nCTU2AneCUl0&rsv_pq=b1d8566c00013654&rsv_sug3=26&rsv_sug1=22&rsv_sug7=100&rsv_sug2=0&rsv_sug4=8057",
"https://fanyi.baidu.com/?aldtype=16047#en/zh/component",
"https://www.youtube.com/watch?v=5dsGWM5XGdg",
"https://www.youtube.com/channel/UC9egiwuJsQZ0Cy2to5fvSIQ",
"https://www.youtube.com/results?search_query=cat",
"https://github.com/caemasar/ChapterGeneration",
"https://blog.csdn.net/iiseeyou/article/details/80757715",
"https://github.com/rg3/youtube-dl",
"https://www.jianshu.com/p/8817a7b0c8d6",
"http://www.yujzw.com/python/python-youtube-dl.html"]

for web in webList:
    print(web)
    webbrowser.open(web)
#webbrowser.open("http://www.baidu.com")