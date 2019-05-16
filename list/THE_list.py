from ImportModules import *

url = "https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2019_limit0_7216a250f6ae72c71cd09563798a9f18.json"
r = requests.get(url)

j = json.loads(r.text)
universities = j["data"]
THE_list = []

for i in range(100):
	rank = universities[i]["rank"].replace("=", "")
	name_without_the = universities[i]["name"].replace("the", "")
	name_without_comma = name_without_the.replace(",", "")
	name_without_acronym_at_the_back = re.sub(r"\([^)]*\)", "", name_without_comma)
	name = name_without_acronym_at_the_back.strip()
	university = [name, rank]
	add_to_sorted(THE_list, university, 0, len(THE_list))