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

workbook = xlsxwriter.Workbook('results.xlsx')
worksheet = workbook.add_worksheet('urls')

for website in website_list:
    print(space + '\n' + website + '\n' + space)
    likely_pages = [website + '/contact', website + '/contact-us', website + '/about', website + '/about-us']
    website_phone_numbers = []
    website_internal_urls = []
    website_email_address = []
    for likely_page in likely_pages:
        website_internal_urls.append(likely_page)
    try:
        driver.get(website)
    except:
        print("Error retreiving website")
    html_page = driver.page_source
    page_soup = soup(html_page, 'html.parser')
    string_soup = str(page_soup)

    try:
        website_not_found = page_soup.find("div", {"id": "main-message"})
        website_not_found = website_not_found.text.strip()
    except:
        try:
            website_not_found = page_soup.find("title")
            website_not_found = website_not_found.text.strip()
        except:
            website_not_found = "website found!"

    if "this site can't" or '404' not in website_not_found:
        for link in page_soup.findAll('a', attrs={'href': re.compile("^http://")}):
            url = str(link.get('href'))
            if url in website_internal_urls:
                pass
            else:
                if 'contact' in url:
                    website_internal_urls.append(url)
                elif 'about' in url:
                    website_internal_urls.append(url)

        for page in website_internal_urls:
            try:
                driver.get(page)
            except:
                print("Error retreiving page: " + page)
            else:
                html_page = driver.page_source
                page_soup = soup(html_page, 'html.parser')
                string_soup = str(page_soup)

                phone_list = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', string_soup)
                for phone_number in phone_list:
                    if phone_number in website_phone_numbers:
                        pass
                    else:
                        if '-' in phone_number:
                            website_phone_numbers.append(phone_number)
                        elif '(' in phone_number:
                            website_phone_numbers.append(phone_number)
                        elif '.' in phone_number:
                            phone_number_frame = phone_number.split('.')
                            try:
                                section1 = phone_number_frame[0]
                                section2 = phone_number_frame[1]
                                section3 = phone_number_frame[2]
                            except:
                                pass
                            else:
                                if len(section1) == 3:
                                    if len(section2) == 3:
                                        if len(section3) == 4:
                                            website_phone_numbers.append(phone_number)
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                        else:
                            pass

                email_list = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", string_soup)
                for email in email_list:
                    period_list = []
                    email = email.lower()
                    if email in website_email_address:
                        pass
                    else:
                        if '-' in email:
                            pass
                        else:
                            if '@' in email:
                                email_check = email.split('@')[1]
                    for letter in email_check:
                        if letter == '.':
                            period_list.append(letter)
                    try:
                        if period_list[1] == '.':
                            pass
                    except:
                        if email not in website_email_address:
                            website_email_address.append(email)

        # print(website_internal_urls)
        if website_phone_numbers != []:
            for i in website_phone_numbers:
                print('phone_number found: ' + i)
        else:
            print("No Phone Number Found")
        if website_email_address != []:
            for i in website_email_address:
                print('Email found: ' + i)
        else:
            print("No Email Address Found")
    else:
        print("Unable to find website")

    worksheet.write_column('A1', url_list)
    print("[*]Excel Sheet Saved")
    workbook.close()
print(space + "\nBBB url spider has finished spinning its web, Looks like we've got some flies!\nSUCCESS!\n" + space)
driver.quit()
sys.exit()
