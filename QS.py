import re, json, requests

url = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/397863.txt?_=1557926919488"
r = requests.get(url)

j = json.loads(r.text)
universities = j["data"]

with open("QS.csv", "w", encoding = "utf-8") as outfile:
	for university in universities:
		rank = university["rank_display"].replace("=", "")
		name_without_comma = university["title"].replace(",", "")
		name_without_acronym_at_the_front = re.sub(r"[^-]*-", "", name_without_comma)
		name_without_acronym_at_the_back = re.sub(r"\([^)]*\)", "", name_without_acronym_at_the_front)
		name = name_without_acronym_at_the_back.strip()
		country = university["country"].replace(",", "")
		outfile.write(rank + "," + name + "," + country + "\n")