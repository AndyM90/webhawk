# -*- coding: utf-8 -*-

# IMPORTED LIBRARIES
from __future__ import print_function
from __future__ import division
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import xlsxwriter
import time
import sys

# ENCODING
reload(sys)
sys.setdefaultencoding('utf8')

'''
NOTES GO HERE:

'''

website_list = []
website_grader = 'https://website.grader.com/'
space = "*" * 75
CHROME_OPTIONS = Options()
# CHROME_OPTIONS.add_argument('--headless')
CHROME_OPTIONS.add_argument('--no-sandbox')
CHROME_OPTIONS.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=CHROME_OPTIONS)

seo_list = []
grade_list = []
mobile_list = []
security_list = []
performance_list = []

workbook = xlsxwriter.Workbook('website_grades.xlsx')
worksheet = workbook.add_worksheet('results')
cell_format = workbook.add_format({'bold': True, 'font_color': 'black'})

for website in website_list:
    print(space + '\n' + website + '\n' + space)
    try:
        driver.get(website_grader)
    except:
        print("Error retreiving website")
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[1]/label')
    element.send_keys(website)
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/button').click()
    time.sleep(10)
    html_page = driver.page_source
    page_soup = soup(html_page, 'html.parser')
    try:
        no_result = page_soup.find('h1', {"class": "main-error-text"})
        no_result = no_result.text.strip()
    except:
        no_result = "Info Found!"
    if "Well, that didn't go" in no_result:
        print("No results for this search")
    else:
        try:
            pop_up = page_soup.find('a', {"class": "icon icon-cancel"})
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/header/a').click()
        except:
            pass
        grade_container = page_soup.find('div', {"class": "radial-inner-container"})
        grade = grade_container.text.strip()
        print("Website Grade: " + grade)
        try:
            performance_container = page_soup.find('span', {"data-reactid": ".0.0.4.0.0.0.0.0"})
            performance = performance_container.text.strip()
            print("Performance: " + performance + "/30")
        except:
            driver.refresh()
            time.sleep(8)
            try:
                pop_up = page_soup.find('a', {"class": "icon icon-cancel"})
                driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/header/a').click()
            except:
                pass
            html_page = driver.page_source
            page_soup = soup(html_page, 'html.parser')
            try:
                grade_container = page_soup.find('div', {"class": "radial-inner-container"})
                grade = grade_container.text.strip()
                print("Website Grade: " + grade)
            except:
                grade = "Not found!"
                print("Website Grade: " + grade)
            try:
                mobile_container = page_soup.find('span', {"data-reactid": ".0.0.5.0.0.0.0.0"})
                mobile = mobile_container.text.strip()
                print("Mobile: " + mobile + "/30")
            except:
                mobile = "Not found!"
                print("Mobile: " + mobile)
            try:
                seo_container = page_soup.find('span', {"data-reactid": ".0.0.6.0.0.0.0.0"})
                seo = seo_container.text.strip()
                print("seo: " + seo + "/30")
            except:
                seo = "Not found!"
                print("seo: " + seo)
            try:
                security_container = page_soup.find('span', {"data-reactid": ".0.0.7.0.0.0.0.0"})
                security = security_container.text.strip()
                print("security: " + security + "/10")
            except:
                security = "Not found!"
                print("security: " + security)
            try:
                performance_container = page_soup.find('span', {"data-reactid": ".0.0.4.0.0.0.0.0"})
                performance = performance_container.text.strip()
                print("performance: " + performance + "/10")
            except:
                performance = "Not found!"
                print("Performance: " + performance)
        else:
            mobile_container = page_soup.find('span', {"data-reactid": ".0.0.5.0.0.0.0.0"})
            mobile = mobile_container.text.strip()
            print("Mobile: " + mobile + "/30")
            seo_container = page_soup.find('span', {"data-reactid": ".0.0.6.0.0.0.0.0"})
            seo = seo_container.text.strip()
            print("seo: " + seo + "/30")
            security_container = page_soup.find('span', {"data-reactid": ".0.0.7.0.0.0.0.0"})
            security = security_container.text.strip()
            print("security: " + security + "/10")
    seo_list.append(seo)
    grade_list.append(grade)
    mobile_list.append(mobile)
    security_list.append(security)
    performance_list.append(performance)
worksheet.write('A1', 'WEBSITE', cell_format)
worksheet.write('B1', 'GRADE', cell_format)
worksheet.write('C1', 'PERFORMANCE', cell_format)
worksheet.write('D1', 'SEO', cell_format)
worksheet.write('E1', 'SECURITY', cell_format)
worksheet.write('F1', 'MOBILE', cell_format)
worksheet.write_column('A2', website_list)
worksheet.write_column('B2', grade_list)
worksheet.write_column('C2', performance_list)
worksheet.write_column('D2', seo_list)
worksheet.write_column('E2', security_list)
worksheet.write_column('F2', mobile_list)
workbook.close()
driver.quit()
print(space + "\nWEBSITE GRADE RETREIVER HAS FINISHED EXECUTION\nSUCCESS!\n" + space)
