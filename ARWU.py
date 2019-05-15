from bs4 import BeautifulSoup
import requests

url = "http://www.shanghairanking.com/ARWU2018.html"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table")
rows = table.find_all("tr")[1:]

with open("ARWU.csv", "w", encoding = "utf-8") as outfile:
	for row in rows:
		cols = row.find_all("td")
		rank = cols[0].string
		name = cols[1].a.string.replace("," , "")
		country = cols[2].a.get("title")[21:]
		trimmed_country = country.replace(".", "")
		outfile.write(rank + "," + name + "," + trimmed_country + "\n")
		
url = "http://www.shanghairanking.com/ARWU2018Candidates.html"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table")
rows = table.find_all("tr")[1:]

with open("ARWU.csv", "a", encoding = "utf-8") as outfile:
	for row in rows:
		cols = row.find_all("td")
		rank = cols[0].string
		name = cols[1].string.replace(",", "")
		country = cols[2].img.get("title")
		outfile.write(rank + "," + name + "," + country + "\n")