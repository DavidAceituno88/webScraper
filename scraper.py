from bs4 import BeautifulSoup
import requests

url  = "https://www.mwcbarcelona.com/agenda/speakers"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="speaker-card__meta")

for list in lists:
    name = list.find('strong', class_="block font-medium text-white").text
    about = list.find('span', class_="ais-Highlight-nonHighlighted")
  
    info = [name, about]
    print(info)
