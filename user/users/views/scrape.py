from random import randint
import requests
from bs4 import BeautifulSoup
import random


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
    WRESTLER_URLS = add_wreslters_urls(10, 10000, 10, CAGEMATCH_SEARCH_URL) # So, here, Among 100 different pages, with iteration of 10 (third agument).
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

def infos(option, search, list_links, searching) ->  str:
    index = list_links.index(option)
    informations = "https://www.cagematch.net/"+search[index].find('a')['href'] # Column link in wrestler page
    page = requests.get(informations, headers={'Accept-Encoding': 'identity'})
    soup = BeautifulSoup(page.text, 'html.parser')    
    searching.append(soup.findAll('td', {'class':['TCol', 'TColSeparator']})) # Titles infos
    result = soup.find_all("td") 
    result2 = soup.find_all("a") 

    return result2

def append_list_link_contents(soup, WRESTLER_OVERVIEWS, list_links) -> str:
    search_two = soup.findAll('li', {'class':['ContentNavigatorItem']}) # Contents infos
    for j in search_two: 
        list_links.append(j.text) 
    return search_two

def from_link_list(search, list_links, searching, option):
    lists = list()
    lists2 = list()
    date = infos(option, search, list_links, searching)
    search = searching[0]
 
    for i in date:
        if option == "Career": 
            for j in i("img"):
                c = i["href"]
                d = j["alt"]
                a = c + d

                lists.append(c)
                lists.append(":")
                lists.append(d)
    
        if option == "Tournaments": # a
            pass
    return lists


def main_function(career_list, tournament_list) -> list:
    
    WRESTLERS_OVERVIEWS = []

    link_list = []

    searching = []
    
    CAGEMATCH_SEARCH_URL = "https://www.cagematch.net/?id=2&view=workers&search"

    RANDOM_URL = generate_random_urls_pages(CAGEMATCH_SEARCH_URL)

    soup = accept_url(CAGEMATCH_SEARCH_URL)
    
    LIST_GIMMICK_URL = url_number(soup)
    
    result_number_url = random_individual_wrestler_url(soup, LIST_GIMMICK_URL)

    info_url = wrestler_gimmick_url(soup, result_number_url)
    append_list_link(WRESTLERS_OVERVIEWS, info_url)

    search = append_list_link_contents(info_url, WRESTLERS_OVERVIEWS, link_list)
    try:
        career_list.append(from_link_list(search, link_list, searching, "Career"))

        from_link_list(search, link_list, searching, "Tournaments")
    except ValueError:
        pass
    # print(tournament_list)
    return WRESTLERS_OVERVIEWS

"""
l = []
c = []
main_function(l, c)
print(l, c)

"""