# scrape Diane Rehm's transcripts
# uses python 2.7.x

from bs4 import BeautifulSoup as bs
import urllib2
import datetime
import nltk
import time

PAUSE = 10
ONE_DAY = datetime.timedelta(days=1)
URL_STEM = 'http://thedianerehmshow.org'
START_DATE = datetime.date(2013, 06, 01)
END_DATE = datetime.date.today()

# Collect the following: 
description_urls = []
transcript_urls = []
transcripts = []

# make URLs for description pages
def makeurls():
  targetdate  = START_DATE 
  while targetdate < END_DATE:
    urlstring  = (URL_STEM + '/shows/' + targetdate.strftime('%Y-%m-%d'))
    description_urls.append(urlstring)
    targetdate += ONE_DAY

# grab url's of individual show transcripts given the URL of the description page
# There are usually two transcripts per description page
def scrapetransurls():
  for url in description_urls:
    try:
      description_page = bs(urllib2.urlopen(url))
      trans_anchors = description_page.findAll('a', {'title' : 'View the transcript'})
      for anchor in trans_anchors:
        transcript_urls.append(str(URL_STEM + anchor.get('href')))
      time.sleep(PAUSE)
    except:
      pass

# grab the transcript content, spoken only--not metadata, and write it to a text file
def scrapetranscripts():
  for url in transcript_urls:
    transpage = bs(urllib2.urlopen(url))
    trans_content = transpage.findAll('div', {'class' : 'trans-event-content'})
    f = open((url[34:44] + url[45:50] +  '_rehm.txt'), 'w') 
    f.write(nltk.clean_html(str(trans_content)))
    f.close()
    time.sleep(PAUSE)

makeurls()
scrapetransurls()
scrapetranscripts()
