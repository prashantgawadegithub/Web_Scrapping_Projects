from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.airbnb.co.in/s/New-Delhi--India/homes?adults=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes"

r=requests.get(url)
# print(r)

soup=BeautifulSoup(r.text,"lxml")
# print(soup)

# np=soup.find("a",class_="l1ovpqvx c1ytbx3a dir dir-ltr").get("href")
# # print(np)
# cnp = "https://www.airbnb.co.in"+np
# # print(cnp)

# # getting url of multiple pages

# while True:
#     np=soup.find("a",class_="l1ovpqvx c1ytbx3a dir dir-ltr").get("href")
#     # print(np)
#     cnp = "https://www.airbnb.co.in"+np
#     # print(cnp)
#     url =cnp
#     r=requests.get(url)
#     soup=BeautifulSoup(r.text,"lxml")

# # extracting data from single page
#
# Names = []
# Price = []
# Desc = []
# Reviews = []
#
# names = soup.find_all("div", class_="t1jojoys dir dir-ltr")
# # print(names)
# for i in names:
#     n = i.text
#     Names.append(n)
# print(len(Names))
#
# prices = soup.find_all("div", class_="_1jo4hgw")
# # print(prices)
# for i in prices:
#     p = i.text
#     Price.append(p)
# print(len(Price))
#
# desc = soup.find_all("span", class_="t6mzqp7 dir dir-ltr")
# # print(desc)
# for i in desc:
#     d = i.text
#     Desc.append(d)
# print(len(Desc))
#
# reviews = soup.find_all("span", class_="r1dxllyb dir dir-ltr")
# # print(reviews)
# for i in reviews:
#     r = i.text
#     Reviews.append(r)
# print(len(Reviews))
#
# df=pd.DataFrame({"Name":Names,"Prices/night":Price,"stay Description":Desc})
# print(df)


for i in range(1,15):

    names = soup.find_all("div",class_="t1jojoys dir dir-ltr")
    # print(names)
    for i in names:
        n=i.text
        Names.append(n)
    print(len(Names))

    prices = soup.find_all("div",class_="_1jo4hgw")
    # print(prices)
    for i in prices:
        p=i.text
        Price.append(p)
    print(len(Price))

    desc = soup.find_all("span",class_="t6mzqp7 dir dir-ltr")
    # print(desc)
    for i in desc:
        d=i.text
        Desc.append(d)
    print(len(Desc))

    reviews = soup.find_all("span",class_="r1dxllyb dir dir-ltr")
    # print(reviews)
    for i in reviews:
        r=i.text
        Reviews.append(r)
    print(len(Reviews))

    np=soup.find("a",class_="l1ovpqvx c1ytbx3a dir dir-ltr").get("href")
    # print(np)
    cnp = "https://www.airbnb.co.in"+np
    # print(cnp)
    url =cnp
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")

df=pd.DataFrame({"Name":Names,"Prices/night":Price,"stay Description":Desc})
print(df)