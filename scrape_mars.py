from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pandas
import requests
import PyMongo

def init_browser():
    executable_path = {
        "executable_path": "chromedriver.exe"
        return Browser("chrome", **executable_path, headless=False)
    }
    
def scrape():
    browser = init_browser()
    mars_mission ={}
    
    url="https://mars.nasa.gov/news/"
    response = requests.get(url)
    browser.visit(url)
    #html = browser.html
    soup = bs(response.content, 'html.parser')
    news_title = soup.find_all(class_='content_title')[0]
    news_title=news_title.text.strip()
    news_p=soup.find_all(class_='rollover_description_inner')[0]
    news_p=news_p.text.strip()

    jpl = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(jpl)
    jpl_response= requests.get(jpl)
    jpl_soup = bs(jpl_response.content, 'html.parser')
    [type(item) for item in list(jpl_soup.children)]
    button =browser.find_by_text(" FULL IMAGE")
    button.click()
    feat_img=jpl_soup.find_all('a')[2]
    feat_img=feat_img.text.strip()
    browser.quit()

    m_facts = "https://space-facts.com/mars/"
    tables = pd.read_html(m_facts)
    tables

    m_facts_df = tables[0]
    m_facts_df.columns = ['Factoid', 'Measurement']
    m_facts_df['Factoid'] = m_facts_df['Factoid'].str.replace(':', '')
    m_facts_html = m_facts_df.to_html()

    cerberus = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced#open"
    schiaparelli = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced#open"
    syrtis = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced#open"
    valles = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced#open"

    hemisphere_image_urls = [{"title":"Cerberus", "img_url": cerberus},
        {"title":"Schiaparelli", "img_url":schiaparelli},
        {"title":"Surtis", "img_url":syrtis},
        {"title":"Valles", "img_url":valles}
    ]

        for x in range(len(hemisphere_image_urls)):
        print(hemisphere_image_urls[x]['title'])
        print(hemisphere_image_urls[x]['img_url'] + '\n')
    
