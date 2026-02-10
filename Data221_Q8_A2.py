from bs4 import BeautifulSoup
import requests

h2_html = requests.get("https://en.wikipedia.org/wiki/Data_science").text
parsed_h2 = BeautifulSoup(h2_html, "html.parser")

heading2 = parsed_h2.find("div", id="mw-content-text")
if heading2 is None:
    print("Main content not found")
    exit()

parser_output = heading2.find("div", class_="mw-parser-output")
if parser_output is None:
    print("Parser output not found")
    exit()

exclude = ["References", "External links", "See also", "Notes"]
headings = []

for h2 in parser_output.find_all("h2"):
    text = h2.get_text(strip=True)
    text1 = text.replace("[edit]", "").strip()

    if any(word in text1 for word in exclude):
        continue

    headings.append(text1)

# Write headings to file
with open("headings.txt", "w", encoding="utf-8") as f:
    for heading in headings:
        f.write(heading + "\n")





