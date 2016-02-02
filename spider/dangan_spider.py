# -*- coding:utf-8 -*- 
#!/usr/bin/python
'''
使用多线程抓取某论坛帖子的url和标题
'''

import requests
from bs4 import BeautifulSoup
import threading

n = 0
url_list = ['http://www.wdzj.com/dangan/xnzx/']

A = 65

def genURL():
	for x in range(A, A + 26):
		ch = chr(x)
		for i in range(1, 100):
			raw_url = 'http://www.wdzj.com/dangan/%s' % (ch + '-' + str(i) + '.html')
		url_list.append(raw_url)

class MyThread(threading.Thread):
	def __init__(self, func, args):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
	def run(self):
		apply(self.func, self.args)
#排名	平台名称	成交量	平均利率	平均借款期限	累计待还金额
#rank	name 	amount		percent	time	return_amount

def get_data(soup):
	table = soup.find_all('table')[1]
	tr_list = table.find_all('tr')
	for tr in tr_list:
		span_list = tr.find_all('span')
		rank = span_list[1].next_element.encode('utf-8')
		name = span_list[2].next_element.encode('utf-8')
		td_list = tr.find_all('td')
		amount = td_list[2].next_element.encode('utf-8')
		percent = td_list[3].next_element.encode('utf-8')
		time = td_list[4].next_element.encode('utf-8')
		return_amount = td_list[5].next_element.encode('utf-8')
		
		s = "%s\t%s\t%s\t%s\t%s\t%s" % (rank, name, amount, percent, time, return_amount)
		with open('/Users/liucancheng/Documents/lcr_github/liucanru.github.io/spider/result.txt', 'a+') as f:
			f.writelines(s)
			f.writelines('\n')

def dangan(soup):
	items = soup.find('ul', 'recordList').find_all('span', 'name')
	for item in items:
		print item.next_element.encode('utf-8')

def running(url):
	# lock.acquire()
	html = requests.get(url, headers = {
	    'Connection': 'Keep-Alive',
	    'Accept': 'text/html, application/xhtml+xml, */*',
	    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
	})
	if html.status_code == 200:
		html_text = html.text
	soup = BeautifulSoup(html_text)
	html = requests.get(url)
	dangan(soup)
	
	"""
		with open('/Users/liucancheng/Documents/lcr_github/liucanru.github.io/spider/result.txt', 'a+') as f:
			for link in soup.find_all('a', 'title'):
				s = 'http://ubuntuforums.org/' + str(link.get('href')) + ' ' + str(link.get_text().encode('utf-8'))
				f.writelines(s)
				f.writelines('\n')
		# lock.release()
	"""

if __name__ == '__main__':
	thread_list = [ MyThread(running, (url, )) for url in url_list ]
	for t in thread_list:
		t.setDaemon(True)
		t.start()
	for i in thread_list:
		i.join()
	print "process ended"
	"""
		# inspect repetition data
		with open('/home/zhg/Pictures/cao.txt', 'r') as f:
			f_list = f.readlines()
			set_list = set(f_list)
		for x in set_list:
			if f_list.count(x) > 1:
				print "the <%s> has found <%d>" % (x, f_list.count(x))
	"""