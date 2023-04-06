from bs4 import BeautifulSoup
import requests
from csv import writer

url  = "https://uxdx.com/usa/2023/speakers"
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('div', class_="grid grid-cols-2 h-56")

with open('speakersUXDS.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)

    header = ['Name','Title','Company']
    thewriter.writerow(header)
    for list in lists:
        name = list.find('p',class_="text-xl font-bold line-clamp-2").text
        title = list.find('p',class_="text-md line-clamp-2").text
        company = getattr(list.find('p',class_="text-md font-medium line-clamp-2"),'text', None)

        info = [name,title,company]
        thewriter.writerow(info)