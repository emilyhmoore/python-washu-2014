# Scraper to collect petition info from petitions.whitehouse.gov
from bs4 import BeautifulSoup
import csv
from nltk.util import clean_html
import urllib2

# What page?
page_to_scrape = 'http://www.washingtonpost.com/blog/monkey-cage/Archive/201408'

# What info do we want?
headers = ["Title", "Author"]

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
print len(titles)
for title in titles:
	p = clean_html(str(title.find("a")))
	print p
authors = soup.findAll("div", attrs={'class':'blog-byline'})
print len(authors)
for author in authors:
	s = clean_html(str(author))
	s = "".join(s.split("By ")[1::])
	print s
dates = soup.findAll("span", attrs={'class':'timestamp'})
print len(dates)
for date in dates:
	d = clean_html(str(date))
	d = "".join(d.split("Posted at ")[1::])
	print d
	
for i in range(47):
	title = titles[i]
	p = clean_html(str(title.find("a")))
	author = authors[i]
	s ="".join(clean_html(str(author)).split("By ")[1::])
	csvwriter.writerow([p, s])
	
readFile.close()