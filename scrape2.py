from turtle import clear
from types import NoneType
import requests
from bs4 import BeautifulSoup
from datetime import date 
from random import randint
import random





class CagematchScraper:
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

    def AppendListLink(self):
        # self.WrestlerGimmickUrl()
        soup = self.FindUrl(self.infoUrl)
        
        search = soup.findAll('div', {'class':['InformationBoxTitle', 'InformationBoxContents']}) # Titles infos
        # print(search)
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
        """
        print("Date C : ", self.DateCareer) 
        print("Alt C : ", self.TournamentsDates) 
        """
    def main_scraping(self):
        self.RandomUrlChoice()
        self.WrestlerGimmickUrl()
        self.InformationsPages()

"""
scraping = CagematchScraper()
scraping.main_scraping()
"""



def accept_url(url) -> BeautifulSoup:
    page = requests.get(url, headers={'Accept-Encoding': 'identity'})
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def add_wreslters_urls(min_main_page, max_min_page, iterate_by, CAGEMATCH_SEARCH_URL) -> list: # from first search page, add urls after.

    WRESTLER_URLS = []
    WRESTLER_URLS.append(CAGEMATCH_SEARCH_URL)
    for i in range(min_main_page, max_min_page, iterate_by):
        WRESTLER_URLS.append("https://www.cagematch.net/?id=2&view=workers&s=" + str(i))
    return WRESTLER_URLS

def generate_random_urls_pages(CAGEMATCH_SEARCH_URL) -> int: # Choose on wrestler among all pages from pervious function.
    WRESTLER_URLS = add_wreslters_urls(10, 10000, 100, CAGEMATCH_SEARCH_URL) # So, here, Among 100 different pages, with iteration of 10 (third agument).
    RANDOM_URL = random.choice(WRESTLER_URLS)
    return RANDOM_URL

def url_number(soup) -> None:
    LIST_GIMMICK_URL = []

    for i in soup.findAll('td', {'class':['TCol AlignCenter TextLowlight']}):
        LIST_GIMMICK_URL.append(i.text)

    return LIST_GIMMICK_URL

def random_individual_wrestler_url(soup, LIST_GIMMICK_URL) -> int: #Choose one wrestler among all urls
    result = None
    for j in LIST_GIMMICK_URL: 
        result = randint(0, 98)
    return result

def wrestler_gimmick_url(soup, result_number_url) -> BeautifulSoup: # wrestler url. Example : https://www.cagematch.net/?id=2&nr=3776&gimmick=Tetsuya+Naito
    search = soup.findAll('td', {'class':['TCol AlignCenter TextLowlight']})
    searching = soup.findAll('tr', {'class':['TRow1', 'TRow2']})
    info = "https://www.cagematch.net/"+searching[result_number_url].find('a')['href']
    info_url = accept_url(info)
    return info_url


def append_list_link(WRESTLERS_OVERVIEWS, soup) -> None:
    search = soup.findAll('div', {'class':['InformationBoxTitle', 'InformationBoxContents']}) # Titles infos
    for i in search:
        WRESTLERS_OVERVIEWS.append(i.text)

    """
    search_two = soup.findAll('li', {'class':['ContentNavigatorItem']}) # Contents infos
    search_two = soup.findAll('li', {'class':['ContentNavigatorItem']}) # Contents infos
    i = 0
    for j in search_two: 
        self.list_links.append(j.text) 
    return search_two
    """




def main_function() -> list:
    
    WRESTLERS_OVERVIEWS = []

    CAGEMATCH_SEARCH_URL = "https://www.cagematch.net/?id=2&view=workers&search"

    RANDOM_URL = generate_random_urls_pages(CAGEMATCH_SEARCH_URL)

    soup = accept_url(CAGEMATCH_SEARCH_URL)
    
    LIST_GIMMICK_URL = url_number(soup)
    
    result_number_url = random_individual_wrestler_url(soup, LIST_GIMMICK_URL)

    info_url = wrestler_gimmick_url(soup, result_number_url)
    append_list_link(WRESTLERS_OVERVIEWS, info_url)

    my_key = {}
    
    position = 1
    this = ""
    d = ""
    my_list = list()

    for i, n in enumerate(WRESTLERS_OVERVIEWS):
        
        if WRESTLERS_OVERVIEWS[i] == "Signature moves:":
            ac = list(WRESTLERS_OVERVIEWS[i+1])

            j = ""
            for a in range(len(ac)):
                if a > 1 and ac[a].isupper() and ac[a-1] != " " and ac[a-1].islower():
                    ac[a-1] += "," 
            
            
    my_list = "".join(ac)


    print(my_list.split(","))


    return WRESTLERS_OVERVIEWS
    # print(f"{WRESTLERS_OVERVIEWS}")

main_function()