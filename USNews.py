import requests
from bs4 import BeautifulSoup

url = "https://www.usnews.com/education/best-global-universities/rankings"
user_agent = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
r = requests.get(url, headers = user_agent)

soup = BeautifulSoup(r.text, "html.parser")

def div_with_sep(tag):
	return tag.name == "div" and tag.get("class") == ["sep"]
	
universities = soup.find_all(div_with_sep)

with open("USNews.csv", "w", encoding = "utf-8") as outfile:
	for university in universities:
		data = university.find_all("div")
		rank = data[4].span.string.replace("#", "").strip()
		title = data[5].h2.a.string
		location = data[5].div.span.string
		outfile.write(rank + "," + title + "," + location + "\n")

# first 59 pages
for i in range(2, 60):
	url = "https://www.usnews.com/education/best-global-universities/rankings?page=" + str(i)
	
	r = requests.get(url, headers = user_agent)

	soup = BeautifulSoup(r.text, "html.parser")
	
	universities = soup.find_all(div_with_sep)

	with open("USNews.csv", "a", encoding = "utf-8") as outfile:
		for university in universities:
			data = university.find_all("div")
			rank = data[4].span.text.replace("#", "").strip()
			if "Tie" in rank:
				rank = rank.replace("Tie", "").strip()
			title = data[5].h2.a.string
			location = data[5].div.span.string
			outfile.write(rank + "," + title + "," + location + "\n")