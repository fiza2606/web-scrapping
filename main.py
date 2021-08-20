import requests
from bs4 import BeautifulSoup
url ="https://codewithharry.com"

#step 1: get the html
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#step 2: parse the html
soup =  BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#step 3: Html tree traversal

#commonly used types of objects:
#1. Tag
# 2. Navigable string
# 3. BeautifulSoup
# 4 commenttitle = soup.title
#print(type(title.string))
#print(type(title))
#print(type(soup)) 

#Get the title of the HTML page
title = soup.title

#get all the paragraphs of the page
#paras = soup.find_all('p')
#print(paras)

#get all the anchor tags of the page
anchors = soup.find_all('a')
print(anchors)

