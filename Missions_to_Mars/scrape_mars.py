import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    news = soup.find('div', class_='list_text')
    news_title = news.find('div', class_='content_title').text
    news_p = news.find('div', class_='article_teaser_body').text
    browser.quit()
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    src = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = url+src
    browser.quit()
    
    url = "https://galaxyfacts-mars.com/"
    table = pd.read_html(url)
    mars_facts_df = table[0]
    mars_facts_df.columns = ['Mars - Earth Comparison', 'Mars', 'Earth']
    mars_facts_df = mars_facts_df.set_index('Mars - Earth Comparison')
    mars_facts_df = mars_facts_df.drop(['Mars - Earth Comparison'])
    facts_html = mars_facts_df.to_html()
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://marshemispheres.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    descriptions = soup.find_all('div', class_='description')
    hemisphere_image_urls = []
    counter = 0
    for description in descriptions:
        browser.find_by_tag('h3')[counter].click()
    
        html = browser.html
        soup = bs(html, 'html.parser')
    
        title = soup.find('h2', class_='title')
    
        src = soup.find('img', class_='wide-image')['src']
        img_url = url+str(src)
    
        hemisphere_image_urls.append({"title":title.text[:-9], "img_url":img_url})
        counter+=1
        browser.links.find_by_partial_text('Back').click()
    browser.quit()
    mars = {"news_title":news_title, "news_p":news_p, "featured_image_url":featured_image_url, "facts_html":facts_html, "hemisphere_image_urls":hemisphere_image_urls}
    return (mars)