from selenium import webdriver
import time, shutil, os, sys
from google import Google

browser = webdriver.Chrome(executable_path=os.getcwd()+'/mac')

google = Google(browser, 'http://google.com')

google.get('/')

term = input('Deseja pesquisar por... ')

google.search(term)

time.sleep(4)

browser.quit()
