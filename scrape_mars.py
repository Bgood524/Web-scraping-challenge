from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url = 'https://redplanetscience.com/'
    browser.visit(url)
    browser.is_element_present_by_css('div.content_title', wait_time=3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    facts_url = 'https://galaxyfacts-mars.com/'
    browser.visit(facts_url)


    news_p = soup.find_all('div', class_ = 'article_teaser_body')

    news_heading = soup.select_one('div.list_text')
    news_title =news_heading.find('div', class_='content_title').text
    news_p = news_heading.find('div', class_='article_teaser_body').text
    featured_image = soup.find_all('div', class_ = 'list_image')
    featured_image_url = featured_image[0].find("img")["src"]
    tables = pd.read_html(facts_url)
    df = tables[0]
    html_table = df.to_html(index=False)
    image_url = 'https://marshemispheres.com/'
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('div', class_="description")

    image_urls=[]

    for image in images:
        link = image.find('a')
        href = link['href']
        print('https://marshemispheres.com/'+ href)
        image_urls.append('https://marshemispheres.com/'+ href)

    
    hemisphere_image_urls = []
    for url in image_urls:

        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        image = soup.find('img', class_ = 'wide-image')
        image_url= 'https://marshemispheres.com/'+image['src']
        title_tag = soup.find('h2', class_='title')
        title= title_tag.text
        hemisphere_image_urls.append({"title": title,
        'img_url': image_url})
    

    
    mars_collection = {
        'news_title' : news_title,
        'news_p' : news_p,
        'featured_image_url': featured_image_url,
        'html_table': html_table,
        'hemisphere_image_urls' : hemisphere_image_urls
    }   

    browser.quit()

    
    return mars_collection



