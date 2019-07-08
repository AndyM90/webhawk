# -*- coding: utf-8 -*-

# IMPORTED LIBRARIES
from __future__ import print_function
from __future__ import division
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import xlsxwriter
# import time
import re
import sys

# ENCODING
reload(sys)
sys.setdefaultencoding('utf8')

'''
NOTES GO HERE:

'''

# ZIP CODE LIST
# ADD THE LIST OF ZIP CODES YOU WANT TO SCRAPE HERE
website_list = []
space = "*" * 75
CHROME_OPTIONS = Options()
# CHROME_OPTIONS.add_argument('--headless')
CHROME_OPTIONS.add_argument('--no-sandbox')
CHROME_OPTIONS.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=CHROME_OPTIONS)
working_sites = []
go_daddy_list = []
dan_domain_list = []
one_domain_list = []
word_press_list = []
ip_not_found_list = []

workbook = xlsxwriter.Workbook('working url test.xlsx')
worksheet = workbook.add_worksheet('urls')

for website in website_list:
    print(space + '\n' + website + '\n' + space)
    driver.get(website)
    try:
        driver.get(website)
    except:
        print("Error retreiving website")
    html_page = driver.page_source
    page_soup = soup(html_page, 'html.parser')
    try:
        go_daddy_flag = page_soup.find('span', {"style": "font-weight:bold; font-family:GD Boing; font-size: 16px;"})
        go_daddy_flag = go_daddy_flag.text.strip()
    except:
        try:
            word_press_flag = page_soup.find('div', {'class': 'entry-content'})
            word_press_flag = word_press_flag.text.strip()
        except:
            try:
                name_not_resolved = page_soup.find('div', {'id': 'main-message'})
                name_not_resolved = name_not_resolved.text.strip()
            except:
                try:
                    dan_site = page_soup.find('div', {'class': 'col-sm-13 col-md-15 col-lg-16'})
                    dan_site = dan_site.text.strip()
                except:
                    try:
                        one_site = page_soup.find('title')
                        one_site = one_site.text.strip()
                    except:
                        working_sites.append(website)
                    else:
                        if 'Hosted By One.com' in one_site:
                            one_domain_list.append(website)
                else:
                    if 'is for sale!' in dan_site:
                        dan_domain_list.append(website)
            else:
                if "This site can't be rea" in name_not_resolved:
                    ip_not_found_list.append(website)
        else:
            if 'Welcome to WordPress. This is your first post' in word_press_flag:
                word_press_list.append(website)
    else:
        if 'This Web page is parked for FREE' in go_daddy_flag:
            go_daddy_list.append(website)

print(space + '\n' + space)
print('Go Daddy List: ' + " " .join(go_daddy_list))
print(space + '\n' + space)
print('Word Press List: ' + " " .join(word_press_list))
print(space + '\n' + space)
print('Name Not Resolved List: ' + " " .join(ip_not_found_list))
print(space + '\n' + space)
print('Dan Domain List: ' + " " .join(dan_domain_list))
print(space + '\n' + space)
print('One Domain List: ' + " " .join(one_domain_list))
print(space + '\n' + space + '\n' + space + '\n' + space + '\n' + space + '\n' + space)
print('Working urls: ' + " " .join(working_sites))
driver.quit()
