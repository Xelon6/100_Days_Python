import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"

response = requests.get(url,timeout=5)
html = response.text

soup = BeautifulSoup(html, 'html.parser')


search1 = str(input("Please Enter 2 Keywords to search for\n> "))
search2 = str(input("> "))


myLinks=soup.find_all("span",{"class":"titleline"})
Found=False
print("Your Results:")
for link in myLinks:
    
    text = link.find("a").string
    
    if search1 in text or search2 in text:
        print(text)
        Found = True

if not Found:
    print("No results found for your Search")
