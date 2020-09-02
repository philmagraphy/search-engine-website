from bs4 import BeautifulSoup
import requests

pageList = []

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pageList.append(url)

for item in pageList:
    url = "https://venus.cs.qc.cuny.edu/~maph9090/cs355/"
    seedpage = requests.get(url)
    data = seedpage.text

#with open(r'C:\Users\philz\NYU Drive\Documents\Skewl\QC\QC Fall 2019 - Courses\CSCI 355\Term Project\scraper\index.html') as fp:

    soup = BeautifulSoup(data)

    for link in soup.find_all('a'):
        print(link.get('href'))
        print(link.get('title'))

    test = list(soup.stripped_strings)
    print('test' + test[1])

#for string in soup.stripped_strings:
#    print(string)
