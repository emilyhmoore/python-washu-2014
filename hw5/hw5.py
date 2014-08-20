# Scraper to collect petition info from petitions.whitehouse.gov
from bs4 import BeautifulSoup
import csv
from nltk.util import clean_html
import urllib2
import re

# What page?
page_to_scrape = 'http://www.washingtonpost.com/blog/monkey-cage/Archive/201408'

# What info do we want?
headers = ["Title", "Author", "Publish Date", "URL","Is_Post","Comments"]

# Where do we save info?
filename = "monkey-cage-blogs.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

# Open webpage
webpage = urllib2.urlopen(page_to_scrape)

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

# Extract titles on page
titles = soup.findAll("h2", attrs={'class':'entry-title'})
#print len(titles)
for title in titles:
	p = clean_html(str(title.find("a")))
#	print p

authors = soup.findAll("div", attrs={'class':'blog-byline'})
#print len(authors)
for author in authors:
	s = clean_html(str(author))
	s = "".join(s.split("By ")[1::])
#	print s

dates = soup.findAll("span", attrs={'class':'timestamp'})
#print len(dates)
for date in dates:
	d = clean_html(str(date))
	d = "".join(d.split("Posted at ")[1::])
#	print d
	
theurls = soup.findAll("a", attrs={'href':re.compile("^http://www.washingtonpost.com/blogs/monkey-cage/wp/2014/08")})
theurls=theurls[::3]
for i in range(len(theurls)):
	u=theurls[i]
	u=u["href"]
#	print u
	
for i in range(51):
	title = titles[i]
	p = clean_html(str(title.find("a")))
	author = authors[i]
	s ="".join(clean_html(str(author)).split("By ")[1::])
	date=dates[i]
	d="".join(clean_html(str(date)).split("Posted at ")[1::])
	url=theurls[i]["href"]
	u=theurls[i]["href"]
	csvwriter.writerow([p, s, d, u])
	
readFile.close()