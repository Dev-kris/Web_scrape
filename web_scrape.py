from urllib.request import urlopen as uReq
from bs4 import  BeautifulSoup as soup
import time
import sys

welcome = "Indeed job search application. \n"
for characters in welcome:
    sys.stdout.write(characters)
    sys.stdout.flush()
    time.sleep(0.025)

user = input("Please Enter Your Name ")

print ("Welcome %s, this tool was created to find new job postings quickly. \n" %(user))

print ("Current supported countries: France, Porgugal, Spain. \n")

    
country_input = input ("Enter Country ").lower()
location_input = input("Enter Location ").lower()
terms_input = input("Enter Search Term ").lower()

#append correct country code to url
for country_code in country_input:
    country_code = []
    if country_input == "france":
        country_code = ".fr/jobs?q="
    elif country_input == "portugal":
        country_code = ".pt/ofertas?q="
    elif country_input == "italy":
        country_code = ".com/offerte-lavoro?q="
    else:
        print ("Sorry %s is not supported yet"%(country_input))
        exit()

my_url = "https://www.indeed" + country_code + terms_input + "&l=" + location_input + "&sort=date"

#open and download the page
uClient = uReq(my_url)
page_dump = uClient.read()
uClient.close

#parse the html
page_soup = soup(page_dump, "html.parser")

#grabs each job
containers = page_soup.findAll("div",{"class":"jobsearch-SerpJobCard"})

#create csv file to store data
filename = "jobs.csv"
f = open(filename, "w" )
headers = "Job, Company, Location \n"

f.write(headers)

# print each job title and company name and write to csv file
for container in range(len(containers)):
    title_container = containers[container].find("div",{"class": "title"})
    company_container = containers[container].find("span",{"class": "company"})
    
    
    print("Job Title: " + title_container.text.strip())
    print("Company:   " + company_container.text.strip())
    print("Location:  " + country_input + "\n")

    f.write(title_container.text.replace(",", "|").strip() + "," + company_container.text.replace(",", "|").strip() + "," + country_input + "\n" )

f.close()
