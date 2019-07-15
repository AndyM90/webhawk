# -*- coding: utf-8 -*-

# IMPORTED LIBRARIES
from __future__ import print_function
from __future__ import division
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import xlsxwriter
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
inactive_list = []
dead_list = []
yes_list = []
no_list = []
redo_list = []
CHROME_OPTIONS = Options()
# CHROME_OPTIONS.add_argument('--headless')
CHROME_OPTIONS.add_argument('--no-sandbox')
CHROME_OPTIONS.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=CHROME_OPTIONS)

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet('urls')

for website in website_list:
    print(space + '\n' + website + '\n' + space)
    try:
        driver.get(website)
    except:
        print("Error retreiving website")
    page_status = raw_input("Does this website look like it may belong to a pro? ").lower()
    if page_status == "back":
        position = website_list.index(website)
        position = position - 1  # try to merge this line with the lina above it
        redo = website_list[position]
        redo_list.append(redo)
        print("Added " + redo + " to the end of the list so that you can reclassify this website again.")

    if page_status == "yes":
        page_status = "y"
    elif page_status == "no":
        page_status = "n"
    elif page_status == "inactive":
        page_status = "i"
    elif page_status == "dead":
        page_status = "d"

    if page_status == "y":
        print("You have classified " + website + " as a possible pro website\nNow moving to next page...")
        yes_list.append(website)
    elif page_status == "n":
        print("You have classified " + website + " as a bad fit\nNow moving to next page...")
        no_list.append(website)
    elif page_status == "i":
        print("You have classified " + website + " as an inactive domain\nNow moving to next page...")
        inactive_list.append(website)
    elif page_status == "d":
        print("You have classified " + website + " as a dead domain\nNow moving to next page...")
        dead_list.append(website)

for redo in redo_list:
    for i in yes_list:
        if i == redo:
            website_list.remove(redo)
    for i in no_list:
        if i == redo:
            website_list.remove(redo)
    for i in inactive_list:
        if i == redo:
            website_list.remove(redo)
    for i in dead_list:
        if i == redo:
            website_list.remove(redo)
    try:
        driver.get(redo)
    except:
        print("Error retreiving website")
    page_status = raw_input("Does this website look like it may belong to a pro? ").lower()
    if page_status == "yes":
        page_status = "y"
    elif page_status == "no":
        page_status = "n"
    elif page_status == "inactive":
        page_status = "i"
    elif page_status == "dead":
        page_status = "d"

    if page_status == "y":
        print("You have classified " + website + " as a possible pro website\nNow moving to next page...")
        yes_list.append(website)
    elif page_status == "n":
        print("You have classified " + website + " as a bad fit\nNow moving to next page...")
        no_list.append(website)
    elif page_status == "i":
        print("You have classified " + website + " as an inactive domain\nNow moving to next page...")
        inactive_list.append(website)
    elif page_status == "d":
        print("You have classified " + website + " as a dead domain\nNow moving to next page...")
        dead_list.append(website)

yes_count = str(len(yes_list))
no_count = str(len(no_list))
inactive_count = str(len(inactive_list))
dead_count = str(len(dead_list))
worksheet.write_column('A1', yes_list)
worksheet.write_column('B1', no_list)
worksheet.write_column('C1', inactive_list)
worksheet.write_column('D1', dead_list)
workbook.close()
print("[*]Excel Sheet Saved\nPage classification is now finished!\nGood sites: " + yes_count + "\nBad sites: " + no_count + "\nInactive sites: " + inactive_count + "\nDead sites: " + dead_count + "\nClosing chromedriver now.")
driver.close()
