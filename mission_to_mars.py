#!/usr/bin/env python
# coding: utf-8


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser
    
  
def scrape():
    browser = init_browser()
    mars_dict = {}

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    #find the news titles and paragraph data

    space_data = soup.find_all('div', class_ = "list_text")

    news_titles = []
    news_p = []
    for slide in space_data:
        headline_tile = slide.find('a').text
        news_tease = slide.find('div', class_ = 'article_teaser_body').text
        news_titles.append(headline_tile)
        news_p.append(news_tease)


   

    #get featured img
    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(img_url)

    feat_site = browser.html
    soup = BeautifulSoup(feat_site, 'lxml')

    # declare image url root

    root_url = 'https://www.jpl.nasa.gov'

    pg_header = soup.find_all('div', class_ = 'carousel_items')

    
    for item in pg_header:
        articles = item.find('article')
        footer = articles.find('footer')
        link = footer.find('a')
        img_path = link['data-fancybox-href']

    featured_img_url = root_url + img_path
      



        #Mars Weather. scrape the latest Mars weather tweet from the page

    tweet_site = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(tweet_site)

    tweet_site = browser.html
    soup = BeautifulSoup(tweet_site, 'lxml')

    tweets = soup.find_all('ol', class_ = "stream-items js-navigable-stream")

    for tweet in tweets:
        section = tweet.find('div', class_ = "content")
        sect_loc = section.find('div', class_= "js-tweet-text-container")
        weather = sect_loc.find('p').get_text()
        
        

    #Mars Facts. use Pandas to scrape the table containing facts about the planet

    # facts_site = 'https://space-facts.com/mars/'
    # browser.visit(facts_site)

    # facts_site = browser.html
    # soup = BeautifulSoup(facts_site, 'lxml')

    # facts_table = soup.find_all('table')

    # mars_facts = pd.read_html(str(facts_table))

    # #convert to dataframe and drop index
    # mars_facts_df = mars_facts[0]
    # mars_facts_df.columns = ['Fact', 'Values']

    # mars_facts_df.set_index('Fact', drop = True, inplace = True)

    # #convert new dataframe to dictionary

    # mars_table_all = mars_facts_df.to_dict()

    # for _, vals in mars_table_all.items():
    #     mars_table = vals
        #print(mars_table)
    


    
    # ### Mars Hemispheres
     # obtain high resolution images for each of Mar's hemispheres.

    hemis_site = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_site)

    hemis_site = browser.html
    soup = BeautifulSoup(hemis_site, 'lxml')

    #get the urls and image names for each hemisphere.
    # Step 1 get the hemisphere names and the link to each hemisphere page
    results = soup.find_all('div', class_ = "item")
    base_url = 'https://astrogeology.usgs.gov'

    hemi_nm  = []
    hemi_url = []
    for result in results:
        desc = result.find('div', class_ = "description")
        links_all = desc.find('a', class_ = "itemLink product-item")
        link = links_all['href']
        title  = links_all.find('h3').text
        full_link = base_url + link
        hemi_url.append(full_link)
        hemi_nm.append(title)

  
    # step 2: get the url for the full image by looping through hemi_url and using splinter to navigate to each page
    #then scraping the page

    img_base_url = 'https://astrogeology.usgs.gov'
    large_img_url = []

    for link in hemi_url:
        link_text = link
        img_site = f"{link_text}"
        browser.visit(img_site)
        img_site = browser.html
        soup = BeautifulSoup(img_site, 'lxml')
        hemi_info = soup.find_all('div', class_ = "wide-image-wrapper ")
        for item in hemi_info:
            image = item.find('img', class_ = "wide-image")['src']
            full_img_url = img_base_url + image
            large_img_url.append(full_img_url)
            print(full_img_url)


    #combine hemisphere name and image url into a dictionary

    hemisphere_img_urls = dict(zip(hemi_nm,large_img_url ))

    hemisphere_img_urls 

    mars_dict = {"mars_headlines": news_titles,
                "news_desc": news_p,
                "featured_img": featured_img_url,
                "weather": weather,
                "mars_hemispheres": hemisphere_img_urls
                     }

    return mars_dict

 # "featured_img": recent_news,
                # "weather": marsweather,



