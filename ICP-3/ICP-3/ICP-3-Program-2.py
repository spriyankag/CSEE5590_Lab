import requests
import urllib.request
import os
from bs4 import BeautifulSoup

#URL link for the url_code
url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#Getting the requets from web page
html_page = requests.get("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")

html_page_1 = urllib.request.urlopen(url)

# using beautiful soup for html parser
soup = BeautifulSoup(html_page.text, "html.parser")

# print title of the page
print(soup.title.string)

#print all the web links from the page
for i in soup.find_all('a'):
    print(i.get('href'))


th_list = []

#print table contents
for rows in soup.find_all('table', class_='wikitable sortable plainrowheaders') :

    rows_1 = rows.find_all('tr')
    for row in rows_1:
        td = row.find_all("td")
        for i in td:
            print(i.text)

            th = row.find("th")
            if th.text not in th_list:
                th_list.append(th.text)
                print("State or Union Territory:  ", th.text)













