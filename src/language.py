#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : language.py                        #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/unikers               #
# Python version : 2.7                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

from bs4 import BeautifulSoup as parser

def main(cookie, url, config):
	try:
		response = config.httpRequest(url+'/language.php', cookie).encode('utf-8')
		html = parser(response, 'html.parser')
		for x in html.find_all('a'):
			if 'Bahasa Indonesia' in str(x):
				config.httpRequest(url+x['href'], cookie)
				break
	except: pass