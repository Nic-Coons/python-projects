from bs4 import BeautifulSoup
import requests
import re

url = ("pythonprogramming.net/about")

r = requests.get("http://"+url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

#for link in soup.find_all('a'):
    #print(link.get('href'))
pattern = re.compile(r'important')
print soup.find('p', text=pattern)
