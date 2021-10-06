from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    browser.is_element_present_by_css('div.content_title', wait_time=3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    news_p = soup.find_all('div', class_ = 'article_teaser_body')

    news_heading = soup.select_one('div.list_text')
    news_title =news_heading.find('div', class_='content_title').text
    news_p = news_heading.find('div', class_='article_teaser_body').text
    
    return {
        'news_title' : news_title,
        'news_p' : news_p
    }   



