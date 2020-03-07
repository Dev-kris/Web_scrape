from urllib.request import urlopen as uReq
from bs4 import  BeautifulSoup as soup

terms_input = input("Enter Search Terms ").lower()
country_input = input ("Enter Country ").lower()
location_input = input("Enter Location ").lower()

#append correct country code to url
for country_code in country_input:
    country_code = []
    if country_input == "france":
            country_code = ".fr/jobs?q="
    elif country_input == "portugal":
        country_code = ".pt/ofertas?q="
    elif country_input == "spain":
        country_code = ".es/ofertas?q="
    elif country_input == "germany":
        country_code = ".pt/ofertas?q="
    elif country_input == "italy":
        country_code = ".com/offerte-lavoro?q="
    else:
        print ("Sorry " +country_input + " is not supported yet")
        break

my_url = "https://www.indeed" + country_code + terms_input + "&l=" + location_input + "&sort=date"

#open and download the page
uClient = uReq(my_url)
page_dump = uClient.read()
uClient.close

#parse the html
page_soup = soup(page_dump, "html.parser")

#grabs each job
containers = page_soup.findAll("div",{"class":"jobsearch-SerpJobCard"})



# print each job title and company name
for container in range(len(containers)):
    title_container = containers[container].find("div",{"class": "title"})
    company_container = containers[container].find("span",{"class": "company"})
    #location_container = containers[container].find("div",{"class": "location"})
    print("Job Title: " + title_container.text.strip())
    print("Company:   " + company_container.text.strip())
    #print("Location:  " + location_container.text.strip())
    print(" ")

    
#for container in range(len(containers)):
    #company_container = containers[container].find("div",{"class": "sjcl"})
    #print("Company: " + company_container.text.strip())