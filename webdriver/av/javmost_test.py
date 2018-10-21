import requests
from bs4 import BeautifulSoup
from selenium import webdriver

if __name__ == '__main__':
    # res = requests.get('https://www5.javmost.com/SDDE-329/', verify=False)
    # doc = BeautifulSoup(res.text, features='lxml')
    # src = doc.select_one('#player1').get('src')
    browser = webdriver.Chrome("C:\TianBaSoft\soft\chromedriver.exe")
    browser.get('https://www5.javmost.com/SDDE-329/')
    browser.find_element_by_css_selector('#player1')