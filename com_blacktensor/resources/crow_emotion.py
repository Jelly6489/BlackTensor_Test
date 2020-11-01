# import requests
# from bs4 import BeautifulSoup
# import json
# import re
# import sys
# import time, random
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

# url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=코알라'

# r = requests.get(url)
# html = r.content
# soup = BeautifulSoup(html, 'html.parser')
# titles_html = soup.select('.new_area > a.news_tit')

# for i in range(len(titles_html)):
#     print(i+1, titles_html[i].text)

##################################################################################################################################################

###  HeadLine
# # pip install lxml
# import requests
# from bs4 import BeautifulSoup

# def naver_news(keyword, order):
    
#     a = ''
    
#     for i in range(20)[1:]:
#         url = r'https://search.naver.com/search.naver?&where=news&query={}&sm=tab_pge&sort={}&&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=287&start={}&refresh_start=0'.format(keyword, order, 10*(i-1)+1)
#         resp = requests.get(url)
#         soup = BeautifulSoup(resp.text, 'lxml')
#         article_title = soup.find_all('a', class_ = 'news_tit')
        
#         for j in article_title:
#             a += j.get_text()
            
#     return a

# return_ = naver_news('삼성전자', 1)
# print(return_)
        
        
##################################################################################################################################################
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd
import re

# title_text = ''
# link_text = ''
# source_text = ''
# date_text = ''
# contents_text = ''

def main():
    info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+" 시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
    maxpage = input("최대 크롤링할 페이지 수 입력하시오: ")
    query = input("검색어 입력: ")
    sort = input("뉴스 검색 방식 입력(관련도순=0 최신순=1 오래된순=2): ") #관련도순=0 최신순=1 오래된순=2
    s_date = input("시작날짜 입력(2019.01.04):") #2019.01.04
    e_date = input("끝날짜 입력(2019.01.05):") #2019.01.05
    crawler(maxpage, query, sort, s_date, e_date)
main()

def crawler(maxpage, query, sort, s_date, e_date):
    s_from = s_date.replace(".","")
    e_to = e_date.replace(".","")
    page = 1
    maxpage_t =(int(maxpage)-1)*10+1 # 11= 2페이지 21=3페이지 31=4페이지 ...81=9페이지 , 91=10페이지, 101=11페이지

    while page <= maxpage_t:
        url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
        response = requests.get(url)
        html = response.text

        #뷰티풀소프의 인자값 지정
        soup = BeautifulSoup(html, 'html.parser')

        #태그에서 제목과 링크주소 추출
        atags = soup.select('.news_tit')
        for atag in atags:
            title_text.append(atag.text) #제목
            link_text.append(atag['href']) #링크주소

        #신문사 추출
        source_lists = soup.select('.thumb_box')
        for source_list in source_lists:
            source_text.append(source_list.text) #신문사

        #날짜 추출
        date_lists = soup.select('.info')
        for date_list in date_lists:
            test=date_list.text
            date_cleansing(test) #날짜 정제 함수사용

        #본문요약본
        contents_lists = soup.select('a.api_txt_lines.dsc_txt_wrap')
        for contents_list in contents_lists:
            #print('==='*40)
            #print(contents_list)
            contents_cleansing(contents_list) #본문요약 정제화

        #모든 리스트 딕셔너리형태로 저장
        result= {"date" : date_text , "title":title_text , "source" : source_text ,"contents": contents_text ,"link":link_text }
        print(page)

        df = pd.DataFrame(result) #df로 변환
        page += 10

#날짜 정제화 함수
def date_cleansing(test):
    try:
        #지난 뉴스
        #머니투데이 10면1단 2018.11.05. 네이버뉴스 보내기
        pattern = '\d+.(\d+).(\d+).' #정규표현식
        r = re.compile(pattern)
        match = r.search(test).group(0) # 2018.11.05.
        date_text.append(match)
    except AttributeError:
        #최근 뉴스
        #이데일리 1시간 전 네이버뉴스 보내기
        pattern = '\w* (\d\w*)' #정규표현식

        r = re.compile(pattern)
        match = r.search(test).group(1)
        #print(match)
        date_text.append(match)

#내용 정제화 함수
def contents_cleansing(contents):
    first_cleansing_contents = re.sub('<dl>.*?</a> </div> </dd> <dd>', '',
    str(contents)).strip() #앞에 필요없는 부분 제거
    second_cleansing_contents = re.sub('<ul class="relation_lst">.*?</dd>', '',
    first_cleansing_contents).strip()#뒤에 필요없는 부분 제거 (새끼 기사)
    third_cleansing_contents = re.sub('<.+?>', '', second_cleansing_contents).strip()
    contents_text.append(third_cleansing_contents)
    #print(contents_text)


#엑셀로 저장하기 위한 변수
RESULT_PATH ='C:/Users/User/Desktop/python study/beautifulSoup_ws/crawling_result/' #결과 저장할 경로
now = datetime.now() #파일이름 현 시간으로 저장하기
# 새로 만들 파일이름 지정
outputFileName = '%s-%s-%s %s시 %s분 %s초 merging.xlsx' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
df.to_excel(RESULT_PATH+outputFileName,sheet_name='sheet1')




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
