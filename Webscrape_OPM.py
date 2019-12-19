# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:06:19 2019

@author: Jack
"""

from bs4 import BeautifulSoup
from contextlib import closing
from requests.exceptions import RequestException
from requests import get
import time 
import smtplib
import datetime

phonydate = datetime.date(2019, 11, 16)

todaydate = datetime.datetime.today().weekday()

print()

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return(resp.content)
            else: 
                return None 
    except RequestException as e:
        log_error('Error during requests to {0}:{1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code == 200 
           and content_type is not None 
           and content_type.find('html') > -1)

def log_error(e):
    print(e)

def detect_chapter():
    while True: 
        url = 'http://w12.readonepunchman.net/manga/onepunch-man-chapter-121/'
        
        raw_html = simple_get(url)
        
        processed_html = BeautifulSoup(raw_html, 'html.parser')
        
        chaplist = []
        
        time.sleep(2)
        
        if todaydate == 5:
            for option in processed_html.select('option'):
                if "http://w12.readonepunchman.net/manga/onepunch-man-chapter-" in option['value']:
                    chapter = option['value'][58:-1] #removes all characters but chapter number
                    chaplist.append(chapter)
                        
                else:
                    pass
            
            removed_duplicate = list(dict.fromkeys(chaplist))  
            
            numof_chapters = len(removed_duplicate)
            
            print(numof_chapters) 
            

        
        else: 
            pass
        
    while True: 
    
        nchaplist = []
        
        time.sleep(3)
        
        if todaydate == 5:
            for option in processed_html.select('option'):
                if "http://w12.readonepunchman.net/manga/onepunch-man-chapter-" in option['value']:
                    chapter = option['value'][58:-1] #removes all characters but chapter number
                    nchaplist.append(chapter)
                        
                else:
                    pass
            nremoved_duplicate = list(dict.fromkeys(chaplist))  
        
            nnumof_chapters = len(nremoved_duplicate)
            
            if nnumof_chapters > numof_chapters:
                print('new chapter')
    
        else: 
            pass
        

detect_chapter()
