from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('li', class_="slide")


    news = {}
    #     Loop through returned results
    for result in results:
    # Error handling
        try:
        # Identify and return news title
            news_title = result.find('div', class_='content_title').text
            # Identify and return paragraph text
            news_p = result.div.find("div", class_="article_teaser_body").text
            # Identify and return date
            news_date = result.find('div',class_='list_date').text

            # Print results only if title, price, and link are available
            if (news_title and news_p and news_date):
                
                # print('Title :',news_title)
                # print('Paragraph :', news_p)
                news = {'Title' :news_title, 'Paragraph' :news_p, 'Date' : news_date }
                return news

    #                 browser.click_link_by_text('More')
        except AttributeError as e:
            print(e)


   


    # JPL Mars Space Images - Featured Image

    browser.quit()


    


    browser = init_browser()

    


    url_JPL= "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


    


    browser.visit(url_JPL)


    




    html_JPL = browser.html
    soup = BeautifulSoup(html_JPL, 'html.parser')

    results = soup.find_all('li', class_="slide")


    JPL = {}
    #     Loop through returned results
    for result in results:
    # Error handling
        try:
        # Identify and return news title
            featured_image_url = result.find('div', class_='img').img['src']
    #             # Identify and return paragraph text
            featured_image_description = result.find('div', class_='img').img['title']
    #             # Identify and return date
    #             news_date = result.find('div',class_='list_date').text

            # Print results only if title, price, and link are available
            if (featured_image_url and featured_image_description ):
                JPL = {'Image description':featured_image_description, 'Image URL':featured_image_url }
                return JPL


    #                 browser.click_link_by_text('More')
        except AttributeError as e:
            print(e)


    


    # Mars Weather twitter scrape


  


    browser.quit()


    


    browser = init_browser()


    


    url_weather = "https://twitter.com/marswxreport?lang=en"


    


    browser.visit(url_weather)


   


    html_weather = browser.html
    soup = BeautifulSoup(html_weather, 'html.parser')

    results = soup.find_all('div', class_="stream-container")


    


    #     Loop through returned results
    for result in results:
        # Error handling
        try:
            # Identify and return news title
            mars_weather = result.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    #             # Identify and return paragraph text
    #         featured_image_description = result.find('div', class_='img').img['title']
    #             # Identify and return date
    #             news_date = result.find('div',class_='list_date').text

                # Print results only if title, price, and link are available
            if (mars_weather):
                weather = {'Mars Weather':mars_weather}
                return weather
                    
                    
                    
    #                 browser.click_link_by_text('More')
        except AttributeError as e:
            print(e)


    


    # Mars Facts


    


    browser.quit()


    


    browser = init_browser()

    


    url_facts = "https://space-facts.com/mars/"


    


    browser.visit(url_facts)


   



    html_facts = browser.html
    soup = BeautifulSoup(html_facts, 'html.parser')

    results = soup.find_all("div", class_="widget widget_text profiles")


    


    #     Loop through returned results
    col_1 = []
    col_2 = []
    for result in results:
        # Error handling
        try:
            td_item = result.find_all('td', class_='column-1')
            tr_item = result.find_all('td', class_='column-2')


    #         row = [tr_item.text for tr_item in td_item]
    #         row
            if(td_item and tr_item):
    #             print(td_item,"  ",tr_item)
                for el in td_item:
                    col_1.append(el.get_text())
                for el in tr_item:
                    col_2.append(el.get_text())
            
        except AttributeError as e:
            print(e)


    


    mars_facts_df= pd.DataFrame({'Description':col_1,'Value':col_2})
    mars_facts_df


    


    # HTML table pandas dataframe
    html_table_mars_facts = mars_facts_df.to_html()





    # Mars Hemispheres
    browser.quit()


    


    browser = init_browser()

  


    url_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


   


    browser.visit(url_hemispheres)


  


    html_hemispheres = browser.html
    soup = BeautifulSoup(html_hemispheres, 'html.parser')

    results = soup.div.find_all("h3")

    


    


    hemisphere = []
    for result in results:
        hemisphere.append(result.get_text())
    


 


    


   


    hem_link=[]
    for i in hemisphere:
        browser.click_link_by_partial_text(i)
        html_hemispheres = browser.html
        soup = BeautifulSoup(html_hemispheres, 'html.parser')

        results = soup.find_all('div', class_='downloads')
        for result in results:
            hem_link.append(result.a['href'])
        
        browser.visit(url_hemispheres)
        





    hemisphere_image_urls = []

    for i in range(len(hem_link)):
        hemisphere_image_urls.append({"title": hemisphere[i], "img_url": hem_link[i]})
    
    return hemisphere_image_urls

   




 




