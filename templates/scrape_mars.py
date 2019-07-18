from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def scrape_all():
   executable_path = {"executable_path":"/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless = False)

    news_title, news_p = mars_news(browser)

    # Store data in a dictionary
    news_data = {
        "news_title": news_title,
        "news_p": news_p
    }

    return data

def mars_news(browser):