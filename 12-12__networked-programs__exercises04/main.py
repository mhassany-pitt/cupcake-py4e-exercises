import urllib.request
from bs4 import BeautifulSoup
url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('p')
print("Paragraph tags:", len(tags))
