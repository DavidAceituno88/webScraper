import requests
from bs4 import BeautifulSoup
from csv import writer

mainUrl = 'https://uxdx.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0'
}

r = requests.get('https://uxdx.com/usa/2023/speakers/')
soup = BeautifulSoup(r.content,'html.parser')

speakerList = soup.find_all('a', class_='rounded-lg shadow-xl transform border-gray-50 border border-solid hover:scale-105 transition duration-500 ease-in-out')
speakerLinks = []
for speaker in speakerList:
    link = speaker.get('href')
    speakerLinks.append(mainUrl+link)

with open('speakersUXDS.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)

    header = ['Name','Title','Company','Linkedin']
    thewriter.writerow(header)
    for link in speakerLinks:
        r =requests.get(link,headers=headers)
        soup = BeautifulSoup(r.content,'html.parser')
        name = soup.find('h1', class_='text-4xl pb-2').text
        position = soup.find('p',class_='text-md').text
        company = soup.find('p',class_='text-md font-bold').text
        try:
            linkedin = soup.find('a',class_='text-base mb-2 mr-5').get('href')
        except: 
            linkedin = 'No Linkedin'
        
        speakerInfo = [name,position,company,linkedin]
        thewriter.writerow(speakerInfo)

