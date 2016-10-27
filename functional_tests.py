from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
