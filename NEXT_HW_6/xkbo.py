import csv
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

Chromedriver_path='C:/Users/82108/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

user_data_dir ="C:/Users/82108/Desktop/NEXT/HW/NEXT_HW_6/cash"

chrome_options=Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
service=Service(executable_path=Chromedriver_path)

driver=webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.koreabaseball.com/')

today = datetime.now().strftime('%Y%m%d')

file=open(f'{today}xkbo.csv', mode="w", newline='')
writer=csv.writer(file)
writer.writerow(["rank", "team", "game"])

chart=driver.find_element(By.XPATH, '//*[@id="rankTitle"]')
chart.click()
for i in range(1, 11):
    title=driver.find_element(By.XPATH, f'/html/body/form/div[3]/section[1]/div/div[2]/ul[2]/li[2]/table/tbody/tr[{i}]')
    game=driver.find_element(By.XPATH, f'/html/body/form/div[3]/section[2]/div[1]/div[3]/div/div[1]/ul/li[{i}]/div')


file.close()






