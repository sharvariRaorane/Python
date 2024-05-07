from plyer import notification
import time
import feedparser
import os

news = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")

while True:
    for newsitem in news['items']:
        notification.notify(title="News",message = newsitem['title'],app_icon = os.getcwd()+r"\4363382.ico",timeout = 5,toast = False)
        time.sleep(30)  
