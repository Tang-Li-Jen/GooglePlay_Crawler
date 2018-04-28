import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Install lattest Chrome driver:
# https://sites.google.com/a/chromium.org/chromedriver/downloads
path = '/Users/charlie/Desktop/GooglePlay/' 
driver = webdriver.Chrome(path+'chromedriver')
driver.get('https://play.google.com/store/apps/collection/cluster?clp=wgYpCiUKH2NvbS5iaXRzbWVkaWEuYW5kcm9pZC5tdXNsaW1wcm8QARgDGAE%3D%3AS%3AANO1ljL05bg')

# crawl until the end page
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
	lastCount = lenOfPage
	time.sleep(3)
	lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
	if lastCount==lenOfPage:
		match=True

#for i in range(3):
#	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  
#	time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
domain = 'https://play.google.com'
url = []
app = []
org = []
desc = []
star = []
for element in soup.find_all('a', {"class": "title"}):
    url.append(domain+element.get('href'))
    app.append(element.get('title'))

for element in soup.find_all('a', {"class": "subtitle"}):
    org.append(element.get('title'))
for element in soup.find_all('div', {"class": "description"}):
    desc.append(element.text)
for element in soup.find_all('div', {"class": "tiny-star star-rating-non-editable-container"}):
    star.append(element.get('aria-label').split()[1])

df = pd.DataFrame({'url':url, 'app':app, 'org':org, 'desc':desc, 'star':star})

print len(df)
print df.head()
df.to_csv(path+'MuslimApp.csv', index=False, encoding='utf-8')
driver.close()
