import requests
from bs4 import BeautifulSoup


#ADD URL OF INDEX FOR NOVEL
URL='https://m.wuxiaworld.xyz/The-Second-Coming-of-Gluttony/all.html'
page  = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find(id='chapterlist')


#NAVIGATE TO DESTINATION FOLDER
with open('SCOG/chapterlist', 'a') as fw:
    for i in result.find_all('a'):
        #GET THE BASE URL FOR EACH CHAPTER
        fw.write('https://m.wuxiaworld.co/The-Second-Coming-of-Gluttony/'+i['href']+'\n')


