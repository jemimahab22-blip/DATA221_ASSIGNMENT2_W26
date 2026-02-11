from http.client import responses

import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/Data_science"
headers={"User-Agent": "Mozilla/5.0"}#using mozilla inorder to access the website officially
contents=requests.get(url,headers=headers)
html=contents.text# this is the where i am storing the contents to be requested
soup=BeautifulSoup(contents.text,"html.parser")


title_page=soup.find("title")
print("The article's page title is: ",title_page.text.strip())

#extracting the first page from the article

content_division=soup.find("div",id="mw-content-text")
first_paragraph=content_division.find_all("p")
for paragraph in first_paragraph:
    text=paragraph.text.strip()

    if len(text)>=50: #this filters the short or empty paragraphs
        print(text)
        break  # this stops after the first valid paragraph

