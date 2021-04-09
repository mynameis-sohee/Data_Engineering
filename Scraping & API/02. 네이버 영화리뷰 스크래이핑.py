# 네이버 영화리뷰 스크래이핑

import re
import requests
from bs4 import BeautifulSoup
import numpy as np

BASE_URL = "https://movie.naver.com/movie"


# 페이지 URL을 받아 페이지를 가져오고, BeautifulSoup 으로 파싱한 객체 & requests 을 통해 받은 페이지를 return
def get_page(page_url):
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    return soup, page


# 리뷰 리스트에서 평균 별점을 구해 return
def get_avg_stars(reviews):
    num=[]
    
    for i in reviews:
        num.append(i['review_star'])
    
    num=np.array(num)
    avg=np.mean(num)
    
    return avg


# 영화제목 검색 시 가장 먼저 나오는 영화 Code return
def get_movie_code(movie_title):
    search_url = f"{BASE_URL}/search/result.nhn?query={movie_title}&section=all&ie=utf8"
    page_2 = requests.get(search_url)
    soup_2 = BeautifulSoup(page_2.content, 'html.parser')
    movie_code = int(soup_2.find('p', class_ = 'result_thumb').find('a').get('href').split('=')[1])
    
    return movie_code


# review_num만큼 리뷰 항목이 담긴 리스트를 return
def scrape_by_review_num(movie_title, review_num):
    reviews = []
    i=1
    movie_code = get_movie_code(movie_title)

    while review_num < len(reviews):
        reviews.append(get_reviews(movie_code, i))
        i += 1

    reviews = reviews[:reviews]

    return reviews


# 페이지 수(여기에서는 10)를 기준으로 리뷰를 스크래이핑
def scrape_by_page_num(movie_title, page_num=10):

    reviews = []
    movie_code = get_movie_code(movie_title)
    for i in range(1,page_num+1):
        reviews.append(get_reviews(movie_code, i))

    return reviews
