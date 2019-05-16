from ImportModules import *

url = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/397863.txt?_=1557926919488"
r = requests.get(url)

j = json.loads(r.text)
universities = j["data"]
QS_list = []

for i in range(100):
	rank = universities[i]["rank_display"].replace("=", "")
	name_without_the = universities[i]["title"].replace("the", "")
	name_without_comma = name_without_the.replace(",", "")
	name_without_acronym_at_the_front = re.sub(r"[^-]*-", "", name_without_comma)
	name_without_acronym_at_the_back = re.sub(r"\([^)]*\)", "", name_without_acronym_at_the_front)
	name = name_without_acronym_at_the_back.strip()
	university = [name, rank]
	add_to_sorted(QS_list, university, 0, len(QS_list))