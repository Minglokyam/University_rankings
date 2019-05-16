import re, requests
from bs4 import BeautifulSoup

url = "http://www.shanghairanking.com/ARWU2018.html"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table")
rows = table.find_all("tr")[1:]

with open("ARWU.csv", "w", encoding = "utf-8") as outfile:
	for row in rows:
		cols = row.find_all("td")
		rank = cols[0].string
		name_without_comma = cols[1].a.string.replace("," , "")
		name_without_acronym_at_the_back = re.sub(r"\([^)]*\)", "", name_without_comma)
		name = name_without_acronym_at_the_back.strip()
		country = cols[2].a.get("title")[21:].replace(".", "")
		outfile.write(rank + "," + name + "," + country + "\n")