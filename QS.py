import json
import requests

url = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/397863.txt?_=1557926919488"
r = requests.get(url)

j = json.loads(r.text)
universities = j["data"]

with open("QS.csv", "w", encoding = "utf-8") as outfile:
	for university in universities:
		outfile.write(university["rank_display"] + "," + university["title"].replace("," , "") + "," + university["country"].replace(",", "") + "\n")