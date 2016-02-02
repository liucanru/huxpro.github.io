# -*- coding:UTF-8 -*- 
#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import threading
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

url = 'http://www.wdzj.com/dangan/'
html = requests.get(url, headers = {
	'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0'
})

print html.text
"""
html_text = html.text
soup = BeautifulSoup(html_text)
#soup.prettify()

items = soup.find('ul', 'recordList').find_all('span', 'name')
for item in items:
	print item.get_text().encode('utf-8')

"""