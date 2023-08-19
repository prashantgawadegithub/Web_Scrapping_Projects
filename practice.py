import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# url="https://courses.wscubetech.com/"
url="https://webscraper.io/test-sites/e-commerce/allinone/computers"
# url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
# print(r.status_code)

# url = "https://www.hindustantimes.com/india-news"
# r = requests.get(url)
# print(r.status_code)

# print(r.text)

# # use third url
# # obtaining html using BeautifulSoup
soup = BeautifulSoup(r.text,"lxml")
# print(soup)
# print(soup.div)

# # Tags in html

# print(soup.div.ul)
# print(soup.div.a)
# print(soup.div.p)

# # attributes in html

# tag=soup.div
# tag=soup.header
# print(tag.attrs)

# atb=(tag.attrs)
# print(atb["class"])
# print(atb["role"])

# # Navigable String in HTML

# tag=soup.div.p
# print(tag.string)

# tag=soup.header.div.a.button.span
# print(tag.string)

# # BeautifulSoup - find() Function

# print(soup.find('div'))

# price=soup.find("h4",{"class":"pull-right price"})
# print(price.string)
# desc=soup.find("p",{"class":"description"})
# print(desc.string)
# a=soup.find("p",class_="description")
# print(a.string)

# # BeautifulSoup – findall() with Tags and Attributes

# prices= soup.find_all("h4",class_="pull-right price")
# print(prices)
# print(len(prices))
# print(prices[3])

# for i in prices:
#     print(i.text)

# desc=soup.find_all("p",class_="description")
# print(desc)
# print(len(desc))
# print(desc[3])

# # BeautifulSoup – findall() with RegEx

# data=soup.find_all(["h4","a","p"])
# print(data)

# data=soup.find_all(string="Galaxy Tab 3")
# data=soup.find_all(string="Galaxy Tab")
# data=soup.find_all(string=re.compile("Galaxy"))
# data=soup.find_all(string=re.compile("Idea"))
# print(data)

# # BeautifulSoup – findall() with Pandas

# names=soup.find_all("a",class_="title")
# print(names)

# product_name=[]

# for i in names:
#     name=i.text
#     product_name.append(name)

# print(product_name)

# prices=soup.find_all("h4",class_="pull-right price")

# prices_list = []
# for i in prices:
#     price=i.text
#     prices_list.append(price)

# print(prices_list)

# desc= soup.find_all("p",class_="description")
# desc_list=[]
# for i in desc:
#     desc = i.text
#     desc_list.append(desc)

# print(desc_list)

# reviews = soup.find_all("p",class_="pull-right")
# reviews_list = []

# for i in reviews:
#     rew=i.text
#     reviews_list.append(rew)

# print(reviews_list)

# df=pd.DataFrame({"Product Name":product_name,"Prices":prices_list,"Description":desc_list,"num of reviews":reviews_list})
# print(df)

# df.to_csv("products_details.csv")


## extracting data from nested html tags

# boxes = soup.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")
# print(boxes)
# print(len(boxes))

# box=soup.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")[3]
# print(box)

# name=box.find("a").text
# print(name)

# desc=box.find("p",class_="description").text
# print(desc)

# # use second url->

navbar=soup.find_all("ul",class_="nav",id="side-menu")
# print(navbar)
name=soup.find("li",class_="active")
# print(name)
name1=name.find("a",class_="category-link active")
# print(name1.text)
name2=name.find("ul",class_="nav nav-second-level collapse in")
# print(name2)
name21=name2.find("a",class_="subcategory-link")
print(name21.text)