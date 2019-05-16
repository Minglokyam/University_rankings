import re, json, requests

url = "https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2019_limit0_7216a250f6ae72c71cd09563798a9f18.json"
r = requests.get(url)

j = json.loads(r.text)
universities = j["data"]

with open("THE.csv", "w", encoding = "utf-8") as outfile:
	for university in universities:
		rank = university["rank"].replace("=", "")
		name_without_comma = university["name"].replace(",", "")
		name_without_acronym_at_the_back = re.sub(r"\([^)]*\)", "", name_without_comma)
		name = name_without_acronym_at_the_back.strip()
		country = university["location"]
		outfile.write(rank + "," + name + "," + country + "\n")