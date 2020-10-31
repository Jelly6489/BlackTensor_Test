import requests
from bs4 import BeautifulSoup
import json
import re
import sys
import time, random
# ============================================================
# ==================                     =====================
# ==================         KDD         =====================
# ==================                     =====================
# ============================================================
# class CrowKdd(object):
# def get_url():
# search_keyword = '애플'
# url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_keyword}'

# r = requests.get(url)
# req = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=셀트리온')
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
# news_titles = soup.select('.news .type01 li dt a[title]')

# print('new: ', len(news_titles))
# print()
# for title in news_titles:
#     print(title['title'])

# def get_news(n_url):
#     news_detail = []
#     print(n_url)
#     breq = requests.get(n_url)
#     bsoup = BeautifulSoup(breq.content, 'html.parser')

#     title = bsoup.select('h3#articleTitle')[0].text
#     news_detail.append(title)

#     pdate = bsoup.select('.t11')[0].get_text()[:11]
#     news_detail.append(pdate)

#     _text = bsoup.select('#articleBodyContents')[0].get_text().replace('\n', " ")
#     btext = _text.replace("// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")

#     news_detail.append(btext.strip())

#     pcompany = bsoup.select('#footer address')[0].a.get_text()
#     news_detail.append(pcompany)

#     return news_detail

#     print(news_detail)

# query = "삼성전자"
# s_date = "2020.04.01"
# e_date = "2018.10.30"
# s_from = s_date.replace(".","")
# e_to = e_date.replace(".","")
# page = 1

# f = open("C:/Users/Admin/VscProject/BlackTensor_Test/" + query + '.csv', 'w', encoding='utf-8')

# while page < 100:

#     print(page)

#     url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=1&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)

#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
#     }
#     req = requests.get(url,headers=header)
#     print(url)
#     cont = req.content
#     soup = BeautifulSoup(cont, 'html.parser')
    
#     for urls in soup.select("._sp_each_url"):
#         try :
#             if urls["href"].startswith("https://news.naver.com"):
#                 news_detail = get_news(urls["href"])
#                 f.write("{}\t{}\t{}\t{}\n".format(news_detail[1], news_detail[3], news_detail[0],
#                                                       news_detail[2]))
#         except Exception as e:
#             # print(e) 
#             continue
#     page += 10  
# f.close()

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=코알라'

r = requests.get(url)
html = r.content
soup = BeautifulSoup(html, 'html.parser')
titles_html = soup.select('.new_area > a.news_tit')

for i in range(len(titles_html)):
    print(i+1, titles_html[i].text)


# ============================================================
# ==================                     =====================
# ==================    Preprocessing    =====================
# ==================                     =====================
# ============================================================
# class CrowDf(object):
#     ...
# ============================================================
# ==================                     =====================
# ==================       Modeling      =====================
# ==================                     =====================
# ============================================================
# class CrowDto(db.Model):
#     ...
# class CrowDao(StockDto):
#     ...
# class CrowVo(object):
#     ...
# class CrowTf(object):
#     ...
# class CrowAi(object):
#     ...
# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
