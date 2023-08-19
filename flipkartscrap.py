import requests
from bs4 import BeautifulSoup
import pandas as pd


# # How to Deal with Multiple Pages

# url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
# r=requests.get(url)
# # print(r)
#
# soup = BeautifulSoup(r.text,"lxml")
# # print(soup)
#
# np = soup.find("a",class_="_1LKTO3").get("href")
#     # print(np)
# cnp="https://www.flipkart.com"+np
# print(cnp)



# for i in range(2,11):
#     url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
#     r=requests.get(url)
#     # print(r)
#
#     soup = BeautifulSoup(r.text,"lxml")
#     # print(soup)
#
#     np = soup.find("a",class_="_1LKTO3").get("href")
#         # print(np)
#     cnp="https://www.flipkart.com"+np
#     print(cnp)

# # extracting data from single page

# url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(1)
# r=requests.get(url)
#
#
# soup = BeautifulSoup(r.text,"lxml")
# box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
#
# names=box.find_all("div",class_="_4rR01T")
# # print(names)
#
# Names=[]
# Prices=[]
# Desc=[]
# Reviews=[]
# for i in names:
#     n=i.text
#     Names.append(n)
# # print(Names)
#
# prices=box.find_all("div",class_="_30jeq3 _1_WHN1")
#
# for i in prices:
#     p=i.text
#     Prices.append(p)
# # print(Prices)
#
# desc=box.find_all("ul",class_="_1xgFaf")
# for i in desc:
#     n=i.text
#     Desc.append(n)
# # print(Desc)
#
# reviews=box.find_all("div",class_="_3LWZlK")
# for i in reviews:
#     n = i.text
#     Reviews.append(n)
# # print(Reviews)
# #
# # print(len(Names))
# # print(len(Prices))
# # print(len(Desc))
# # print(len(Reviews))
# df=pd.DataFrame({"product name":Names,"Product Prices":Prices,"Product Desc":Desc,"Product Reviews":Reviews})
# print(df)


# # Extracting data from multiple pages

Names = []
Prices = []
Desc = []
Reviews = []
for i in range(1,21):
    url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r=requests.get(url)


    soup = BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")

    names=box.find_all("div",class_="_4rR01T")
    # print(names)

    for i in names:
        n=i.text
        Names.append(n)
    print(len(Names))

    prices=box.find_all("div",class_="_30jeq3 _1_WHN1")

    for i in prices:
        p=i.text
        Prices.append(p)
    print(len(Prices))

    desc=box.find_all("ul",class_="_1xgFaf")
    for i in desc:
        n=i.text
        Desc.append(n)
    print(len(Desc))

    reviews=box.find_all("div",class_="_3LWZlK")
    for i in reviews:
        n = i.text
        Reviews.append(n)
    print(len(Reviews))


df=pd.DataFrame({"product name":Names,"Product Prices":Prices,"Product Desc":Desc})
print(df)


