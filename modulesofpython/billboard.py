import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.billboard.com/charts/hot-100")
html_content=response.content
soup=BeautifulSoup(html_content,"html.parser")

song=soup.find_all("div",{"class":"chart-row__container"})
rank=soup.find_all("span",{"class":"chart-row__current-week"})


for i,y in  zip(rank,song):
    print(i.text,y.text.replace("\n"," "))
