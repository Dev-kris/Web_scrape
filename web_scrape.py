from urllib.request import urlopen as uReq
from bs4 import  BeautifulSoup as soup

my_url = "https://www.indeed.fr/jobs?q=english&l=Paris+%2875%29&sort=date"

#open and download the page
uClient = uReq(my_url)
page_dump = uClient.read()
uClient.close

#parse the html
page_soup = soup(page_dump, "html.parser")

#grabs each job
containers = page_soup.findAll("div",{"class":"jobsearch-SerpJobCard"})



# print to test containers is scraping correctly
for container in range(len(containers)):
    title_container = containers[container].find("div",{"class": "title"})
    print("Job Title: " + title_container.text.strip())
    