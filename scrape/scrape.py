from turtle import clear
from types import NoneType
import requests
from bs4 import BeautifulSoup
from datetime import date 
from random import randint
import random
import multiprocessing


class Scraping:
    url = "https://www.cagematch.net/?id=2&view=workers&search="
    urls = []
    random_url = None
    page = [None]
    text = [None]
    infoUrl = None
    listGimmickUrl=  [None]
    list_links = []

    WresltersOverviews = []

    searching = None
    
    DateCareer = []
    AltCareer = []

    TournamentsDates = []
    TournamentsAlt = []

    search_two = None

    def FindUrl(self, url):
        page = requests.get(url, headers={'Accept-Encoding': 'identity'})
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def AddWrestlersUrls(self, min, max, number):
        # self.url = "https://www.cagematch.net/?id=2&view=workers&search="
        self.urls.append(self.url)
        for i in range(min, max, number):
            self.urls.append("https://www.cagematch.net/?id=2&view=workers&s=" + str(i))

    def RandomUrlChoice(self):
        self.AddWrestlersUrls(10, 10000, 100)

        self.random_url = random.choice(self.urls) # random url page
        soup = self.FindUrl(self.random_url)
        self.random_url = random.choice(self.urls) # random url page


    def UrlNumber(self, soup):
        for i in soup.findAll('td', {'class':['TCol AlignCenter TextLowlight']}):
            self.listGimmickUrl.append(i.text)


    def Random(self, soup):
        result = None
        for j in self.listGimmickUrl: 
            result = randint(0, 98)
        return result

    def WrestlerGimmickUrl(self):
        self.RandomUrlChoice()
        soup = self.FindUrl(self.random_url)
        search = soup.findAll('td', {'class':['TCol AlignCenter TextLowlight']})
        searching = soup.findAll('tr', {'class':['TRow1', 'TRow2']})
        self.UrlNumber(soup)
        choice = self.Random(soup)
        self.infoUrl = "https://www.cagematch.net/"+searching[choice].find('a')['href']
        print(self.infoUrl)

    def AppendListLink(self):
        # self.WrestlerGimmickUrl()
        soup = self.FindUrl(self.infoUrl)
        search = soup.findAll('div', {'class':['InformationBoxTitle', 'InformationBoxContents']}) # Titles infos
        index = 0
        for i in search:
            index += 1
            self.WresltersOverviews.append(i.text)
        self.search_two = soup.findAll('li', {'class':['ContentNavigatorItem']}) # Contents infos
        search_two = soup.findAll('li', {'class':['ContentNavigatorItem']}) # Contents infos
        i = 0
        for j in search_two: 
            self.list_links.append(j.text) 
        return search_two

    def infos(self, option, search):
        index = self.list_links.index(option[0])
        informations = "https://www.cagematch.net/"+search[index].find('a')['href'] # Column link in wrestler page
        page = requests.get(informations, headers={'Accept-Encoding': 'identity'})
        soup = BeautifulSoup(page.text, 'html.parser')    
        self.searching = soup.findAll('td', {'class':['TCol', 'TColSeparator']}) # Titles infos
        result = soup.findAll('img')	
        return result


    def GenericPageInside(self, soup, option):
        search = self.AppendListLink()
        if option[0] in self.list_links: # if Career in list
            try:
                self.infos(option, search)
            except IndexError:
                print("nan")
        """
        if option[1] in self.list_links: # if Career in list
             try:
                 self.infos(option, 1, search)
             except IndexError:
                 print("nan")
        """
        return search
    def InfoStore(self, soup, option, date_list, alt_list):
        search = self.AppendListLink()
        try:
            iterate = self.infos(option, search)
        except ValueError:
            pass
        try:
            try:
                for ab in self.searching:
                    try:
                        try:
                            try:
                                if option[0] in self.list_links:
                                    date_list.append(ab.text)
                            except ValueError:
                                pass
                         
                        except KeyError:
                            pass
                    except ValueError:
                        print("nononnon")
                for bd in iterate:
                    try:
                        try:
                            try:
                                if option[0] in self.list_links:
                                    alt_list.append(bd["alt"])

                            except ValueError:
                                pass
                         
                        except KeyError:
                            pass
                    except ValueError:
                        print("nononnon")
            except UnboundLocalError:
                pass
        except TypeError:
            print("nan")
        

    def InformationsPages(self):
        soup = self.FindUrl(self.infoUrl)
        options = ["Career"]
        options2 = ["Tournaments"] 
        self.InfoStore(soup, options, self.DateCareer, self.AltCareer)

        self.InfoStore(soup, options2, self.TournamentsDates, self.TournamentsAlt)

        print("Date C : ", self.DateCareer) 
        print("Alt C : ", self.TournamentsDates) 

    def main_scraping(self):
        self.RandomUrlChoice()
        self.WrestlerGimmickUrl()
        self.InformationsPages()

def my_function(num):
    scraping = Scraping()
    scraping.main_scraping()

jobs = []
for i in range(3): # Start 3 Process
    p1 = multiprocessing.Process(target=my_function, args=(i,))
    jobs.append(p1)
        # Declare a new process and pass arguments to i
    p1.start() # starting workers

