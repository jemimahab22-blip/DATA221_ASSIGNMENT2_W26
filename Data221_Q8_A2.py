from os import write

from bs4 import BeautifulSoup
import requests

url="https://en.wikipedia.org/wiki/Data_science"
headers={"User-Agent":"Mozilla/5.0"}
contents=requests.get(url,headers=headers)
html=contents.text
soup=BeautifulSoup(contents.text,"html.parser")

#Extracting all <h2> section headings from the main content area

heading_division = soup.find("div", id="mw-content-text")
all_second_headings=heading_division.find_all("h2")
excluded_headings={"References","External links","See also","Notes"}

# Write headings to file
with open("headings.txt",'w') as file:
    for heading in all_second_headings:
        title=heading.text.replace("[edit]","").strip()
        if title in excluded_headings:
            continue
        file.write(title+"\n")







