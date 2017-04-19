import requests
#from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA&ns=1"

yelp_r = requests.get(url)

print(yelp_r.status_code)

yelp_soup = Beautifulsoup(yelp_r.text, "html.parser")

print(yelp_soup.prettify())