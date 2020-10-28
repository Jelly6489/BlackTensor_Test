import pandas as pd

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13',header=0)[0]

# 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해둠
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

# 회사명과 종목코드 필요 -> 그 이외에 필요 없는 column 제외
code_df = code_df[['회사명', '종목코드']]

# 한글로된 컬럼명을 영어로 변환
code_df = code_df.rename(columns={'회사명' : 'name', '종목코드' : 'code'})
code_df.head() 
print(code_df.head())

# https://finance.naver.com/item/sise.nhn?code=005930(삼성전자)
def get_url(item_name, code_df):
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
    code = code.strip()
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)



    print("요청 URL = {}".format(url))
    return url

# 삼성전자의 일자 데이터 url
item_name='삼성전자' 
url = get_url(item_name, code_df)


# 일자 데이터를 담을 df라는 DataFrame 정의
df = pd.DataFrame()

# 1페이지에서 15페이지의 데이터만 가져오기(약 6개월치)
for page in range(1, 16): 
    pg_url = '{url}&page={page}'.format(url=url, page=page) 
    df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)

# df.dropna()를 이용해 결측값 있는 행 제거
df = df.dropna()

# 한글 -> 영어
df = df.rename(columns= {
    '날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open',
    '고가': 'high', '저가': 'low', '거래량': 'volume'
    })

# 데이터 타입 int 변환
df[['close', 'diff', 'open', 'high', 'low', 'volume']] \
    = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)

# date를 date type 변환
df['date'] = pd.to_datetime(df['date'])

# date 기준으로 내림차순 sort
df = df.sort_values(by=['date'], ascending=False)

# 상위 5개 데이터 확인
df.head()
print(df.head())