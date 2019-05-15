from bs4 import BeautifulSoup
import requests

user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
url = "https://www.usnews.com/education/best-global-universities/rankings"
r = requests.get(url, headers = user_agent)

soup = BeautifulSoup(r.text, "html.parser")

def div_with_sep(tag):
    return tag.name == "div" and tag.get("class") == ["sep"]
	
universities = soup.find_all(div_with_sep)

with open("USNews.csv", "w", encoding = "utf-8") as outfile:
	for university in universities:
		information = university.find_all("div")
		rank = information[4].span.string.replace("#", "").strip()
		name = information[5].h2.a.string.replace(",", "")
		location = information[6].span.string
		outfile.write(rank + "," + name + "," + location + "\n")
		
for i in range(2, 126):
	url = "https://www.usnews.com/education/best-global-universities/rankings?page=" + str(i)
	r = requests.get(url, headers = user_agent)

	soup = BeautifulSoup(r.text, "html.parser")
		
	universities = soup.find_all(div_with_sep)

	with open("USNews.csv", "a", encoding = "utf-8") as outfile:
		for university in universities:
			information = university.find_all("div")
			rank = information[4].span.text.replace("#", "").replace("Tie", "").strip()
			name = information[5].h2.a.string.replace(",", "")
			location = information[6].span.string
			outfile.write(rank + "," + name + "," + location + "\n")