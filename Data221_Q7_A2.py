
import requests
from bs4 import BeautifulSoup

Data_science_html=requests.get("https://en.wikipedia.org/wiki/Data_science").text
parsed_document=BeautifulSoup(Data_science_html,"html5lib")

title_page=parsed_document.find("title")
if title_page:
    print(title_page.get_text(strip=True))
else:
    print("Title tag not found")
paragraph_page=parsed_document.find("div",id="mw-content-text")
if paragraph_page:
    parsed_output=paragraph_page.find("div",class_="mw-body-content")

    if parsed_output:
        for p in parsed_output.find_all("p",recursive=False):
            text=p.get_text(strip=True)
            if len(text)>=50:
                print(text)
                break
    else:
        print("Parser output div not found.")
else:
    print("Main content div not found")
