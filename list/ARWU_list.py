from ImportModules import *

url = "http://www.shanghairanking.com/ARWU2018.html"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table")
rows = table.find_all("tr")[1:]
ARWU_list = []

for i in range(100):
	cols = rows[i].find_all("td")
	rank = cols[0].string
	name_without_comma = cols[1].a.string.replace("," , "")
	name_without_acronym_at_the_back = re.sub(r"\([^)]*\)", "", name_without_comma)
	name = name_without_acronym_at_the_back.strip()
	university = [name, rank]
	add_to_sorted(ARWU_list, university, 0, len(ARWU_list))