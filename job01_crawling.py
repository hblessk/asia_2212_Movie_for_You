from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

options = webdrvier.ChromeOptions()

options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver.exe', options=options)

#겨울왕국1을 본 사람에게
#겨울왕국 2를 추천해주면 볼 것이니. 그런식으로 추천해주는 시스템.

#추천 컨텐츠 목록(마켓컬리, 음악, 영화 등)

url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2022&page=1'



