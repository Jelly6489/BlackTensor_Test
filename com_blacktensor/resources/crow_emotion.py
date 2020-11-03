import requests
import pandas as pd
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from collections import Counter
from com_blacktensor.ext.db import db, openSession, engine

# import time
# import multiprocessing


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

#  HeadLine
class CrowKdd(object):
    # ##keyword = '삼성전자'
    info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+"시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
    maxpage = int(input("최대 크롤링할 페이지 수 입력하시오: "))
    keyword = input("검색어 입력: ")
    order = input("뉴스 검색 방식 입력(관련도순=0 최신순=1 오래된순=2): ") #관련도순=0 최신순=1 오래된순=2
    s_date = input("시작날짜 입력(예: 2020.07.20):")
    e_date = input("끝날짜 입력(예: 2020.10.30):")

    def __init__(self):
        info_main = self.info_main
        maxpage = self.maxpage
        keyword = self.keyword
        order = self.order
        s_date = self.s_date
        e_date = self.e_date

    def naver_news(self, maxpage, keyword, order, s_date, e_date):
        # tag = ['']

        results = []
        # a = ''
        # https://search.naver.com/search.naver?where=news&query={}&sm=tab_opt&sort={}&photo=0&field=0&reporter_article=&pd=3&ds={}&de={}&docid=&nso=so%3Ar%2Cp%3Afrom20201020to20201030%2Ca%3Aall&mynews=0&refresh_start={}&related=0
        # url = r'https://search.naver.com/search.naver?&where=news&query={}&sm=tab_pge&sort={}&photo=0&field=0&reporter_article=&pd=3&ds={}&de={}&docid=&nso=so:da,p:from20201028to20201030,a:all&mynews=0&start={}&refresh_start=0'.format(keyword, order, s_date, e_date, 10*(i-1)+1)
        # url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=1&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
        for i in range(maxpage)[1:]:
            url = r'https://search.naver.com/search.naver?&where=news&query={}&sm=tab_pge&sort={}&photo=0&field=0&reporter_article=&pd=3&ds={}&de={}&docid=&nso=so:da,p:from20201028to20201030,a:all&mynews=0&start={}&refresh_start=0'.format(keyword, order, s_date, e_date, 10*(i-1)+1)
            # url = r'https://search.naver.com/search.naver?&where=news&query={}&sm=tab_pge&sort={}&&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=287&start={}&refresh_start=0'.format(keyword, order, 10*(i-1)+1)
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'lxml')
            if i % 100 == 0:
                print(i,"번째 크롤링")
        #     article_title = soup.find_all('a', class_ = 'news_tit')
            

        #     for j in article_title:
        #         a += j.get_text()
        # return a




            # # title_list = soup.select('.news_tit')
            # title_list = soup.find_all('a', class_ = 'news_tit')

            # for tag in title_list:
            # #     # print(tag.text)
            # #     # df = pd.DataFrame(tag.text)
            # #     # print(df.head())
            #     # results.append(tag.text)
            #     results += tag.get_text()
        # return results

            title_list = soup.find_all('a', class_ = 'news_tit')
            

            for tag in title_list:
                # results += tag.get_text()
                results.append(tag.text)
        return results

    # result = naver_news(object, keyword, 1)
    result = naver_news(object, maxpage, keyword, order, s_date, e_date)
    # print(result)
    df = pd.DataFrame(result)
    # print(df)
    df.columns = ['title']
    print(df.head())
    df.to_csv(keyword + '.csv', encoding='utf8')
'''
0   논어, 새로운 가르침에 겁내지 않으려면 그간의 가르침을 실행해야 한다!       
1  "전 세계 AI 전문가 모여라"…'삼성 AI 포럼 2020' 온라인 개최
2              비트코인 지갑서비스 사업자도 자금세탁방지 의무 부과
3                  [연합뉴스 이 시각 헤드라인] - 12:00
4   “이건희 회장의 ‘도전 DNA’ 계승… 판도 바꾸는 기업으로 진화하자”
'''


# =======================================================================================================================================

# # title_text = []
# # link_text = []
# # source_text = []
# # date_text = []
# # contents_text = []

# def main():
#     info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+" 시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
#     maxpage = input("최대 크롤링할 페이지 수 입력하시오: ")
#     query = input("검색어 입력: ")
#     sort = input("뉴스 검색 방식 입력(관련도순=0 최신순=1 오래된순=2): ") #관련도순=0 최신순=1 오래된순=2
#     s_date = input("시작날짜 입력(2019.01.04):") #2019.01.04
#     e_date = input("끝날짜 입력(2019.01.05):") #2019.01.05
#     crawler(maxpage, query, sort, s_date, e_date)
# main()

# def crawler(maxpage, query, sort, s_date, e_date):
#     s_from = s_date.replace(".","")
#     e_to = e_date.replace(".","")
#     page = 1
#     maxpage_t =(int(maxpage)-1)*10+1 # 11= 2페이지 21=3페이지 31=4페이지 ...81=9페이지 , 91=10페이지, 101=11페이지

#     while page <= maxpage_t:
#         url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
#         response = requests.get(url)
#         html = response.text

#         #뷰티풀소프의 인자값 지정
#         soup = BeautifulSoup(html, 'html.parser')

#         #태그에서 제목과 링크주소 추출
#         atags = soup.select('.news_tit')
#         for atag in atags:
#             title_text.append(atag.text)
#             link_text.append(atag['href'])

#         #신문사 추출
#         source_lists = soup.select('.thumb_box')
#         for source_list in source_lists:
#             source_text.append(source_list.text)

#         #날짜 추출
#         date_lists = soup.select('.info')
#         for date_list in date_lists:
#             test=date_list.text
#             date_cleansing(test)

#         #본문요약본
#         contents_lists = soup.select('a.api_txt_lines.dsc_txt_wrap')
#         for contents_list in contents_lists:
#             #print('==='*40)
#             #print(contents_list)
#             contents_cleansing(contents_list)

#         #모든 리스트 딕셔너리형태로 저장
#         result= {"date" : date_text , "title":title_text , "source" : source_text ,"contents": contents_text ,"link":link_text }
#         print(page)

#         df = pd.DataFrame(result) #df로 변환
#         page += 10

# #날짜 정제화 함수
# def date_cleansing(test):
#     try:
#         pattern = '\d+.(\d+).(\d+).'
#         r = re.compile(pattern)
#         match = r.search(test).group(0) # 2018.11.05.
#         date_text.append(match)
#     except AttributeError:

#         pattern = '\w* (\d\w*)'

#         r = re.compile(pattern)
#         match = r.search(test).group(1)
#         #print(match)
#         date_text.append(match)

# #내용 정제화 함수
# def contents_cleansing(contents):
#     first_cleansing_contents = re.sub('<dl>.*?</a> </div> </dd> <dd>', '',
#     str(contents)).strip()
#     second_cleansing_contents = re.sub('<ul class="relation_lst">.*?</dd>', '',
#     first_cleansing_contents).strip()
#     third_cleansing_contents = re.sub('<.+?>', '', second_cleansing_contents).strip()
#     contents_text.append(third_cleansing_contents)
#     #print(contents_text)


# #엑셀로 저장하기 위한 변수
# RESULT_PATH ='C:/Users/User/Desktop/python study/beautifulSoup_ws/crawling_result/'
# now = datetime.now()

# # 새로 만들 파일이름 지정
# outputFileName = '%s-%s-%s %s시 %s분 %s초 merging.xlsx' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
# df.to_excel(RESULT_PATH+outputFileName,sheet_name='sheet1')
# =======================================================================================================================================

# from bs4 import BeautifulSoup
# import requests

# # url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=삼성전자'
# url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
# # https://search.naver.com/search.naver?where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0
# res = requests.get(url)
# html = res.text

# soup = BeautifulSoup(html, 'html.parser')

# title_list = soup.select('.news_tit')

# for tag in title_list:
#     print(tag.text)

    # ### 네이버 금융 재무정보 크롤링 테스트
    # def NaverCrowStock(self):
    #     url_tmp = 'https://finance.naver.com/item/main.nhn?code%s'
    #     url = url_tmp % ('005930')

    #     item_info = requests.get(url).text
    #     soup = BeautifulSoup(item_info, 'html.parser')
    #     finance_info = soup.select('div.section.cop_analysis div.sub_section')[0]

    #     th_data = [item.get_text().strip() for item in finance_info.select('thead th')]
    #     annual_date = th_data[3:7]
    #     quarter_date = th_data[7:13]

    #     finance_index = [item.get_text().strip() for item in finance_info.select('th.h_th2')][3:0]

    #     finance_data = [item.get_text().stipt() for item in finance_info.select('td')]
    #     finance_data = np.array(finance_data)
    #     finance_data.resize(len(finance_index), 10)

    #     finance_date = annual_date + quarter_date

    #     finance = pd.DataFrame(data=finance_data[0:,0:], index=finance_index, columns = finance_date)


    # ### Nice 평가정보 재무정보 크롤링 테스트
    # def NiceCrow(self):
    #     url_tmp = 'http://media.kisline.com/highlight/mainHighlight.nice?nav=1&paper_stock=%s'
    #     url = url_tmp % ('005930')
    #     tables = pd.read_html(url)
    #     df = tables[4]

# ### Naver 금융 재무정보 2 크롤링 테스트
#     def NaverCrowTmp(self):
#         url_tmp = 'https://finance.naver.com/item/main.nhn?code%s'
#         url = url_tmp % ('005930')
#         tables = pd.read_html(url, encoding='euc-kr')
#         df = tables[3]

# =======================================================================================================================================

# ============================================================
# ==================                     =====================
# ==================    Preprocessing    =====================
# ==================                     =====================
# ============================================================
class CrowDf(object):
    def __init__(self):
        self.ck = CrowKdd()
        this = self.ck
        self.keyword = this.keyword
        print("검색어1: ", self.keyword)

        # this.maxpage = self.maxpage
        # this.keyword = self.ck.keyword
        # this.order = self.order
        # this.s_date = self.s_date
        # this.e_date = self.e_date

        self.word = []
        self.noun_list =[]
        self.positive_word = []
        self.negative_word = []

        self.poflag = []
        self.neflag = []

    # def DataPro(self, keyword, word, positive_word, negative_word, poflag, neflag):
    def DataPro(self):
        # 
        keyword = str(self.keyword)
        word = self.word
        noun_list = self.noun_list
        positive_word = self.positive_word
        negative_word = self.negative_word
        poflag = self.poflag
        neflag = self.neflag
        
        # this = self.ck
        # this.keyword = self.keyword

        # print("검색어2: ", keyword)
        # 
        # word = []
        # noun_list =[]
        # positive_word = []
        # negative_word = []
        # keyword_text = []

        # poflag = []
        # neflag = []

        

        file = open('{}.csv'.format(keyword), 'r', encoding='utf-8')

        # file = open('삼성전자.csv', 'r', encoding='utf-8')
        lists = file.readlines()
        file.close()
        # lists
        
        twitter = Twitter()
        morphs = []

        for sentence in lists:
            morphs.append(twitter.pos(sentence))

        # print(morphs)

        pos = codecs.open('positive_words_self.txt', 'rb', encoding='UTF-8')

        while True:
            line = pos.readline()
            line = line.replace('\n', '')
            positive_word.append(line)
            # keyword_text.append(line)

            if not line: break
        pos.close()

        neg = codecs.open('negative_words_self.txt', 'rb', encoding='UTF-8')

        while True:
            line = neg.readline()
            line = line.replace('\n', '')
            negative_word.append(line)
            # keyword_text.append(line)

            if not line: break
        neg.close()

    # #     # for sentence in morphs : 
    # #     #     for word, text_tag in sentence :
    # #     #         for x in range(len(keyword_text)):
    # #     #             posflag = False
    # #     #             negflag = False

    # #     #             if x < len(positive_word)-1:
    # #     #                 if word.find(keyword_text[x] != -1):
    # #     #                     posflag = True
    # #     #                     print(x, "positive_word?", "테스트 : ", word.find(keyword_text[x]), "비교 단어 : ", keyword_text[x], "인덱스 : ", x, word)
    # #     #                     break
    # #     #             if x > (len(positive_word)-2):
    # #     #                 if word.find(keyword_text[x] != -1):
    # #     #                     negflag = True
    # #     #                     print(x, "negative?","테스트 : ", word.find(keyword_text[i]),"비교단어 : ", keyword_text[i], "인덱스 : ", x, word)
    # #     #                     break

    # #     #                 if posflag == True:
        

    # #     # print(type(positive_word))




    # # #==========================================================================================================
        for sentence in morphs : 
            for word, text_tag in sentence :
                if text_tag in ['Noun']:
                    noun_list.append(word)
                    for x in positive_word:
                        if x == word: 
                            poflag.append(x)
                        
                    for y in negative_word:
                        if y == word:
                            neflag.append(y)

                #         print("부정적 :", y)
                # if text_tag in ['Noun'] and ("것" not in word) and ("내" not in word) and ("첫" not in word) and \
                #     ("나" not in word) and ("와" not in word) and ("식" not in word) and ("수" not in word) and \
                #     ("게" not in word) and ("말" not in word):
                #      noun_list.append(word)
                    
                # if text_tag in ['Noun'] and ("갑질" not in word) and ("논란" not in word) and ("폭리" not in word) and \
                #     ("허위" not in word) and ("과징금" not in word) and ("눈물" not in word) and ("피해" not in word) and \
                #     ("포화" not in word) and ("우롱" not in word) and ("위반" not in word) and ("리스크" not in word) and \
                #     ("사퇴" not in word) and ("급락" not in word) and ("하락" not in word) and ("폐업" not in word) and \
                #     ("불만" not in word) and ("산재" not in word) and ("닫아" not in word) and ("손해배상" not in word) and \
                #     ("구설수" not in word) and ("적발" not in word) and ("침해" not in word) and ("빨간불" not in word) and \
                #     ("취약" not in word) and ("불명예" not in word) and ("구형" not in word) and ("기소" not in word) and \
                #     ("반토막" not in word) and ("호소" not in word) and ("불매" not in word) and ("냉담" not in word) and \
                #     ("문제" not in word) and ("직격탄" not in word) and ("한숨" not in word) and ("불똥" not in word) and \
                #     ("항의" not in word) and ("싸늘" not in word) and ("일탈" not in word) and ("파문" not in word) and \
                #     ("횡령" not in word) and ("사과문" not in word) and ("여파" not in word) and ("울상" not in word) and \
                #     ("초토화" not in word) and ("급감" not in word) and ("우려" not in word) and ("중단" not in word) and \
                #     ("퇴출" not in word) and ("해지" not in word) and ("일베" not in word) and ("이물질" not in word) and \
                #     ("엉망" not in word) and ("소송" not in word) and ("하락" not in word) and ("매출하락" not in word) and \
                #     ("혐의" not in word) and ("부채" not in word) and ("과징금" not in word) and ("포기" not in word) and \
                #     ("약세" not in word) and ("최악" not in word) and ("손실" not in word) and ("의혹" not in word):
                #     positive_word.append(word)

                # elif text_tag in ['Noun'] and ("MOU" not in word) and ("제휴" not in word) and ("주목" not in word) and \
                #     ("호응" not in word) and ("돌파" not in word) and ("이목" not in word) and ("수상" not in word) and \
                #     ("입점" not in word) and ("인기" not in word) and ("열풍" not in word) and ("진화" not in word) and \
                #     ("대박" not in word) and ("순항" not in word) and ("유치" not in word) and ("1위" not in word) and \
                #     ("출시" not in word) and ("오픈" not in word) and ("돌풍" not in word) and ("인싸" not in word) and \
                #     ("줄서서" not in word) and ("대세" not in word) and ("트렌드" not in word) and ("불티" not in word) and \
                #     ("진출" not in word) and ("체결" not in word) and ("증가" not in word) and ("기부" not in word) and \
                #     ("신제품" not in word) and ("신상" not in word) and ("최고" not in word) and ("새로운" not in word) and \
                #     ("착한" not in word) and ("신기록" not in word) and ("전망" not in word) and ("협력" not in word) and \
                #     ("역대" not in word) and ("상승" not in word) and ("늘어" not in word) and ("승인" not in word):
                #     negative_word.append(word)

    # #     # print(noun_list)
        
    # #     # count = Counter(noun_list)
    # #     # words = dict(count.most_common())
    # #     # print(words)
        
    # #     # print(positive_word)
    # #     # print(negative_word)
        count_po = Counter(poflag)
        count_ne = Counter(neflag)
    #     # po_words = count_po.most_common()
        po_words = dict(count_po.most_common())
        ne_words = dict(count_ne.most_common())

        # 워드클라우드로 명사만 추출
        # print(noun_list)
        '''
        ['창립', '주년', '삼성', '전자', '이건희', '회장', '도전', '혁신', '삼성', '전자', '삼성', '포럼', '개최', '김기남', '대표', 
        '핵심', '기술', '발전', '현', '코스피', '코스닥', '장', '동반', '상승', '덕성', '시스', '웍', '한국', '컴퓨터', '삼성', '전자
        ', '창립', '주년', '기념', '개최', '이재용', '부회장', '불참', '롯데', '하이마트', '온라인', '오늘', '역대', '빅', '하트', ' 
        일', '시작', '손연기', '칼럼', '차', '산업혁명', '시대', '문제', '일자리', '삼성', '전자', '모바일', '신제품', '엑시노스', ' 
        ...
        '멘토', '체험', '활동', '김기남', '삼성', '부회장', '로', '코로나', '해결', '위해', '전세계', '연구자', '협력', '순위', '주식
        ', '부자', '위', '눈앞', '이재용', '뉴', '파워', '프라', '마', '규모', '유상증자', '결정', '삼성', '전자', '창립', '주념', ' 
        기념', '회장', '도전', '혁신', '계승', '삼성', '전자', '창립', '주년', '기념', '개최']
        '''

        # 
        print("\n긍정적인 단어 :", po_words)
        # print("긍정적인 단어", positive_word)
        # print(type(po_words))
        print("부정적인 단어 :", ne_words)
        
        word_df = {'positive' : [po_words], 
                   'negative' : [ne_words]}

        df = pd.DataFrame(word_df)

        # df.columns = ['index', 'positive', 'negative']
        print(df.head())
        df.to_csv(keyword + '_word.csv', encoding='utf8')

        '''
        긍정적인 단어 : {'상승': 141, '인기': 66, '출시': 60, '전망': 36, '오픈': 30, 
        '돌파': 19, '트렌드': 12, '체결': 12, '증가': 12, '역대': 11, '협력': 11, 
        '주목': 11, '미소': 8, '기부': 8, '승인': 6, '최고': 6, '대세': 5, '유치': 4, 
        '수상': 4, '불티': 2, '부상': 2, '순항': 2, '호응': 1, '진출': 1}
        부정적인 단어 : {'급감': 233, '여파': 163, '하락': 162, '피해': 115, 
        '직격탄': 83, '논란': 61, '중단': 41, '손실': 39, '반토 막': 34, '최악': 33, 
        '포기': 32, '폐업': 25, '급락': 25, '우려': 24, '불매': 14, '눈물': 13, '
        매각': 10, '호소': 9, '울상': 7, '문제': 6, '불만': 6, '약세': 5, '한숨': 5, 
        '일베': 4, '해지': 4, '초토화': 3, '참혹': 3, '폐점': 2, '파문': 2, 
        '과징금': 2, '항의': 1, '소송': 1, '불명예': 1, '리스크': 1, '갑질': 1, 
        '침해': 1, '발끈': 1}
        '''
# ck = CrowKdd(maxpage, keyword, order, s_date, e_date)

# ck = CrowKdd('maxpage', 'keyword', 'order', 's_date', 'e_date').format(ck.keyword)
# ck = CrowKdd.__init__(keyword)
# print(ck.keyword)



# ============================================================
# ==================                     =====================
# ==================       Modeling      =====================
# ==================                     =====================
# ============================================================
class CrowDto(db.Model):
    __tablename__ = 'stock'
    __table_args__={'mysql_collate' : 'utf8_general_ci'}

    date : str = db.Column(db.String(10), primary_key = True, index = True)
    positive : str = db.Column(db.String(10))
    negative : str = db.Column(db.String(10))
    close : int = db.Column(db.Integer)
    open : int = db.Column(db.Integer)
    volume : int = db.Column(db.Integer)

    def __init__(self, positive, negative, date, close, open, volume):
        self.date = date
        self.close = close
        self.open = open
        self.volume = volume
    
    def __repr__(self):
        return f'Stock(date={self.date}, positive={self.positive}, negative={self.negative}\
             close={self.close}, open={self.open}, volume={self.volume})'

# class CrowVo:
#     date : str = ''
#     close : int = 0
#     open : int = 0
#     volume : int = 0


# Session = openSession()
# session = Session()
# crow_df = CrowDf()


# class CrowDao(StockDto):
    
#     @staticmethod
#     def bulk():
#         Session = openSession()
#         session = Session()
#         crow_df = CrowDf()
#         df = crow_df.hook()
#         # print(df.head())
#         session.bulk_insert_mappings(CrowDto, df.to_dict(orient='records'))
#         session.commit()
#         session.close()

#     @staticmethod
#     def count():
#         return session.query(func.count(CrowDto.date)).one()

#     @staticmethod
#     def save(crow):
#         new_crow = CrowDto(date = crow['date'],
#                            positive = crow['positive'],
#                            negative = crow['negative'],
#                            close = crow['close'],
#                            open = crow['open'],
#                            volume = crow['volume'])
#         session.add(new_crow)
#         session.commit()


# class CrowTf(object):
#     ...
# class CrowAi(object):
#     ...
# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================

# parser = reqparse.RequestParser()

# parser.add_argument('positive', type = str, required = True,
#                             help='This field should be a userId')
# parser.add_argument('negative', type = str, required = True,
#                             help='This field should be a userId')
# parser.add_argument('close', type = str, required = True,
#                             help='This field should be a userId')
# parser.add_argument('open', type = str, required = True,
#                             help='This field should be a userId')
# parser.add_argument('volume', type = str, required = True,
#                             help='This field should be a userId')

# class Crow(Resource):
    
#     @staticmethod
#     def post():
#         args = parser.parse_args()
#         crow = CrowVo()
#         crow.positive = args.positive
#         crow.negative = args.negative
#         crow.close = args.close
#         crow.open = args.open
#         crow.volume = args.volume
#         # service.assign(crow)
#         # print("Predicted Crow")



if __name__ == "__main__":
    ck = CrowKdd()
    cd = CrowDf()
    cd.DataPro()

