import json, requests

url = "https://japanuniversityrankings.jp/data/get?from=0&to=500"
r = requests.get(url)
j = json.loads(r.text)

with open("THE_Japan.csv", "w", encoding = "utf-8") as outfile:
	for university in j:
		outfile.write(str(university["total_rnk"]) + "," + university["jap_name"] + "," + university["total_score_v"] + "\n")
		