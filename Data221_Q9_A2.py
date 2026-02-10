import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Machine_learning"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

# Step 1: main content
content_div = soup.find("div", id="mw-content-text")
if content_div is None:
    print("Main content div not found")
    exit()

parser_output = content_div.find("div", class_="mw-parser-output")
if parser_output is None:
    print("Parser output div not found")
    exit()

tables = parser_output.find_all("table")

selected_table = None

# Step 2: find first table with at least 3 data rows
for table in tables:
    rows = table.find_all("tr")
    if len(rows) >= 4:
        selected_table = table
        break

if selected_table is None:
    print("No suitable table found")
    exit()

rows = selected_table.find_all("tr")

# Step 3: headers
headers_list = []
th_tags = rows[0].find_all("th")

if th_tags:
    headers_list = [th.get_text(strip=True) for th in th_tags]
else:
    col_count = len(rows[1].find_all(["td", "th"]))
    headers_list = [f"col{i+1}" for i in range(col_count)]

# Step 4: table data
table_data = []

for row in rows[1:]:
    cells = row.find_all(["td", "th"])
    row_data = [cell.get_text(strip=True) for cell in cells]

    while len(row_data) < len(headers_list):
        row_data.append("")

    table_data.append(row_data)

# Step 5: save CSV
with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers_list)
    writer.writerows(table_data)


