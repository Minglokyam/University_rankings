import requests
from bs4 import BeautifulSoup

url = "http://www.shanghairanking.com/ARWU2018.html"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find_all("tr")

with open("ARWU.csv", "w", encoding = "utf-8") as outfile:
	for row in table[1:]:
		cols = row.find_all("td")
		university_rank = cols[0].string
		university_name = cols[1].string
		location = cols[2].a.get("title")[21:]
		university_location = location.replace(".", "")
		outfile.write(university_rank + "," + university_name + "," + university_location + "\n")
		
url = "http://www.shanghairanking.com/ARWU2018Candidates.html"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find_all("tr")

with open("ARWU.csv", "a", encoding = "utf-8") as outfile:
	for row in table[1:]:
		cols = row.find_all("td")
		university_rank = cols[0].string
		university_name = cols[1].string
		university_location = cols[2].img.get("title")
		outfile.write(university_rank + "," + university_name + "," + university_location + "\n")