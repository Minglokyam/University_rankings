import json
import requests

url = "https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2019_limit0_7216a250f6ae72c71cd09563798a9f18.json"
r = requests.get(url)

j = json.loads(r.text)
jsonlist = j["data"]

with open("THE.csv", "w", encoding = "utf-8") as outfile:
	for university in jsonlist:
		outfile.write(university["rank"] + "," + university["name"] + "," + university["location"] + "\n")