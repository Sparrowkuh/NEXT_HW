from bs4 import BeautifulSoup as bs
import requests
from openpyxl import Workbook
from datetime import datetime

url='https://finance.naver.com/'

try:
    headers={
        'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Whale/3.25.232.19 Safari/537.36'
    }
    response=requests.get(url, headers=headers)
    
    if response.status_code ==200:
        html_text=response.text
        
        soup=bs(response.text, 'html.parser')
        
        titles=soup.find_all(id='_topItems4')
        titles=list(map(lambda x: x.text.strip(), titles))
        print(titles)
        
        alltitles=soup.find_all(id='_topItems1')
        alltitles=list(map(lambda x: x.text.strip(), alltitles))
        print(alltitles)
        
        articles=soup.find_all(class_='section_strategy')
        articles=list(map(lambda x: x.text.strip(), articles))
        print(articles)
        
        wb=Workbook()
        ws=wb.active
        
        ws. append(["시가총액 상위", "거래상위", "주요쥬스"])
        
        for i, (title, alltitle, article) in enumerate(zip(titles, alltitles, articles), start=1):
             ws.append([i, title, alltitle, article])
        
        today=datetime.now().strftime('%Y%m%d')
        
        filename=f'네이버 증권_chart_{today}.xlsx'
        wb.save(filename)
        print(f"엑셀 파일 저장 완료: {filename}")
                
    else:
        print(f"Error: HTTP 요청 실패. 상태코드: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: 요청 중 오류발생. 오류메세지: {e}")
    