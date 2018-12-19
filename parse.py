# parse.py
# parse super smash bros. ultimate fandom for spirit data, and write to csv

from bs4 import BeautifulSoup
import requests
import csv

filename = "spirits.csv"

class spirit:
    def __init__(self):
        self.name = ""
        self.origin = ""
        self.rating = ""
        self.cat = ""
        self.slots = ""
        self.ability = ""

    def toList(self):
        return [self.name,self.origin,self.rating,self.cat,self.slots,self.ability]


all_spirits = []

link = "https://supersmashbros.fandom.com/wiki/List_of_spirits"
orig = "https://supersmashbros.fandom.com"
links = []
page = requests.get(link)

soup = BeautifulSoup(page.text, 'html.parser')
main_page = soup.find(class_="mw-content-ltr mw-content-text")
for ul in main_page.find_all('ul'):
    for li in ul.find_all('li'):
        for a in li.find_all('a'):
            links.append(orig+a['href'])

for link in links:
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    sec = soup.find(class_="article-table sortable")
    print(link)
    i = 0
    for tr in sec.find_all('tr'):
        if i == 0:
            for th in tr.find_all('th'):
                for text in th:
                    text.replace("<br /","")
                    #print(text.strip()+"\t\t",end='')
        else:
            all_spirits.append(spirit())
            j = 0
            for td in tr.find_all('td'):
                x = str(td.contents[0])
                x = x.replace("<br />","")
                x = x.replace("<br/>","")
                x = x.replace("<i>","")
                x = x.replace("</i>","")
                x = x.strip()
                if j == 0:
                    all_spirits[-1].name = x
                elif j == 1:
                    all_spirits[-1].origin = x
                elif j == 2:
                    all_spirits[-1].rating = x
                elif j == 3:
                    all_spirits[-1].cat = x
                elif j == 4:
                    all_spirits[-1].slots = x
                elif j == 5:
                    all_spirits[-1].ability = x
                j += 1
        i += 1

with open(filename, 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["Spirit","Artwork Origin","Rating","Type","Support Slots","Ability"])
    for sp in all_spirits:
        writer.writerow(sp.toList())

csvFile.close()


