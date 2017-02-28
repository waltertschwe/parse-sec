import requests

from bs4 import BeautifulSoup

page = requests.get("https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent")

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())