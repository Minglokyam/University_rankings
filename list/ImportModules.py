import re, json, requests
from bs4 import BeautifulSoup

def add_to_sorted(list, element, start, end):
	if len(list) == 0:
		list.append(element)
		
	else:
		while start < end:
			middle = (start + end) // 2
			
			if list[middle][0] > element[0]:
				end = middle
			
			else:
				start = middle + 1
			
		list.insert(start, element)