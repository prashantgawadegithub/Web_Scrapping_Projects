import pandas as pd
import requests
from bs4 import BeautifulSoup

# r=requests.get("https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page=1")
# print(r)
# print(r.text)

# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
# r=requests.get("https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page=1",headers=headers)
# print(r)
# print(r.text)
# webpage=r.text

# soup=BeautifulSoup(webpage,'lxml')

# print(soup.prettify())

# companies=soup.find_all("h2",class_="companyCardWrapper__companyName")
# print(companies)
# print(len(companies))
# for i in companies:
    # print(i.text.strip())

# rating=soup.find_all("span",class_="companyCardWrapper__companyRatingValue")
# print(len(rating))
# for i in rating:
    # print(i.text.strip())


# reviews=soup.find_all("span",class_="companyCardWrapper__ActionCount")
# print(len(reviews))
# for i in reviews:
#     print(i.text.strip())


# # another way

# company=soup.find_all("div",class_="companyCardWrapper")
# print(company)
# print(len(company))
#
# Name=[]
# Rating=[]
# Reviews=[]
# Salaries=[]
# Interviews=[]
# Jobs=[]
# Benefits=[]
# Photos=[]
# Description=[]
#
# for i in company:
#
#     Name.append(i.find("h2",class_="companyCardWrapper__companyName").text.strip())
#     Rating.append(i.find("span",class_="companyCardWrapper__companyRatingValue").text.strip())
#     Reviews.append(i.find("span",class_="companyCardWrapper__ActionCount").text.strip())
#     Salaries.append(i.find_all("span",class_="companyCardWrapper__ActionCount")[1].text.strip())
#     Interviews.append(i.find_all("span", class_="companyCardWrapper__ActionCount")[2].text.strip())
#     Jobs.append(i.find_all("span", class_="companyCardWrapper__ActionCount")[3].text.strip())
#     Benefits.append(i.find_all("span", class_="companyCardWrapper__ActionCount")[4].text.strip())
#     Photos.append(i.find_all("span", class_="companyCardWrapper__ActionCount")[5].text.strip())
#     Description.append(i.find("span",class_="companyCardWrapper__interLinking").text.strip())
#
#
# # print(Name)
# print(len(Name))
# # print(Rating)
# print(len(Rating))
# # print(Reviews)
# print(len(Reviews))
# # print(Salaries)
# print(len(Salaries))
# # print(Interviews)
# print(len(Interviews))
# # print(Jobs)
# print(len(Jobs))
# # print(Benefits)
# print(len(Benefits))
# # print(Photos)
# print(len(Photos))
# # print(Description)
# print(len(Description))
#
# d={"Name":Name,"Rating":Rating,"Reviews":Reviews,"Salaries":Salaries,"Interviews":Interviews,"Jobs":Jobs,"Benefits":Benefits,"Photos":Photos,"Description":Description}
#
# df=pd.DataFrame(d)
# print(df)
# print(df.shape)

# # for scraping all pages

final=pd.DataFrame()

for j in range(1,11):

    url="https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={}".format(j)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webpage=requests.get(url,headers=headers).text

    soup=BeautifulSoup(webpage,'lxml')

    company=soup.find_all("div",class_="companyCardWrapper")
    Name = []
    Rating = []
    Reviews = []
    Salaries = []
    Interviews = []
    Jobs = []
    Benefits = []
    Photos = []
    Description = []

    for i in company:
        Name.append(i.find("h2", class_="companyCardWrapper__companyName").text.strip())
        Rating.append(i.find("span", class_="companyCardWrapper__companyRatingValue").text.strip())
        Reviews.append(i.find("span", class_="companyCardWrapper__ActionCount").text.strip())
        Salaries.append(i.find_all("span", class_="companyCardWrapper__ActionCount")[1].text.strip())
        Interviews.append(i.find_all("span", class_="companyCardWrapper__ActionCount")[2].text.strip())
        Jobs.append(i.find_all("span", class_="companyCardWrapper__ActionCount")[3].text.strip())
        Benefits.append(i.find_all("span", class_="companyCardWrapper__ActionCount")[4].text.strip())
        Photos.append(i.find_all("span", class_="companyCardWrapper__ActionCount")[5].text.strip())
        Description.append(i.find("span", class_="companyCardWrapper__interLinking").text.strip())

    d = {"Name": Name, "Rating": Rating, "Reviews": Reviews, "Salaries": Salaries, "Interviews": Interviews,
         "Jobs": Jobs, "Benefits": Benefits, "Photos": Photos, "Description": Description}

    df = pd.DataFrame(d)
    final=final._append(df,ignore_index=True)

print(final)


