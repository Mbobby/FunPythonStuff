#!/usr/bin/python

#My feeble attempt at trying to replace the Curl command-line tool for Unix

"""
	Emmanuel E. Mong
	First thing I did was to check if I have received a command-line argument 
	Next thing to do is to check and verify that the internet is indeed on and functional
	and then parse through the url to make sure it has valid syntax
	finally, retrieve url data through urllib2 and print it on-to the console!
	Walla! Simple and very creative fun! LOL!!
"""

import urllib2
import sys

def internet_is_on():
	try:
		response = urllib2.urlopen('http://www.google.com', timeout = 1)
		return True
	except:
		return False

def parse(string_):
	if(string_[:4] == "http"):
		return string_
	else:
		return "http://" + string_

def main():
	if(len(sys.argv) == 1):
		print "INVALID USAGE: "
		print "Example: fetch www.yahoo.com"
		return 
	if (internet_is_on() == False):
		print "Your internet connection is currently not working properly\nPlease rectify this issue and try again later. \nThanks"
		return
	try:
		response = urllib2.urlopen(parse(sys.argv[1]))
		html = response.read()
		print html
		return
	except:
		print "Invalid Website name entered!! Please check your website name and try again"
		return 

if __name__ == "__main__":
	main()
