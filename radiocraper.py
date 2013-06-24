# scrape WAMU transcripts
# uses python 2.7.x
# To scrape different shows, change constants

from bs4 import BeautifulSoup as bs
import urllib2
import datetime
import time
import os

PAUSE = 10
ONE_DAY = datetime.timedelta(days=1)
URL_STEM = 'http://thekojonnamdishow.org'
START_DATE = datetime.date(2010, 01, 01)
END_DATE = datetime.date.today()
FILE_SUFFIX = '_namdi.txt'

# make directories to collect files in
os.makedirs('corpus')
os.makedirs('trans_collection')

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

# scrape  url's for show transcripts given the URL of the description page
def scrapetransurls():
  for url in description_urls:
    try:
      description_page = bs(urllib2.urlopen(url))
      trans_anchors = description_page.findAll('a', {'title' : 'View the transcript'})
      for anchor in trans_anchors:
        transcript_urls.append(str(URL_STEM + anchor.get('href')))
      print 'collecting urls from: ' + url
      time.sleep(PAUSE)
    except:
      pass

# scrape a clean copy of the transcript, and one with metadata
def scrapetranscripts():
  for url in transcript_urls:
    transpage = bs(urllib2.urlopen(url))
    print 'scraping ' + url
    trans_content = transpage.findAll('div', {'class' : 'trans-event-content'})
    transfile = open('./corpus/' + url[35:45] + url[46:51] +  FILE_SUFFIX, 'w') 
    for speech in trans_content:
      transfile.write(speech.text.encode('utf-8'))
    transfile.close()
    all_content = transpage.find('div', {'id' : 'content'})
    trans_plusmeta = open('./trans_collection/' + url[35:45] + url[46:51] + FILE_SUFFIX, 'w')
    trans_plusmeta.write(all_content.text.encode('utf-8'))
    trans_plusmeta.close()
    time.sleep(PAUSE)

makeurls()
scrapetransurls()
scrapetranscripts()
