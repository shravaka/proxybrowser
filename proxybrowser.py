import sys
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.webdriver import FirefoxProfile

domains = sys.argv[1]

def openSite(filename):

	profile = FirefoxProfile("/home/squid/proxyprofile/")	
	driver = webdriver.Firefox(firefox_profile=profile)
	associated = []
	with open (filename) as f:
		address = f.readline()
		while address:
			driver.get(address)
			for a in driver.find_elements_by_xpath("//a[@href]"):
				associated.append(a.get_attribute("href"))
				if len(associated) == 3 :
					break
			for ap in associated:
				driver.get(ap)	
			associated = []
			address = f.readline()
		driver.close()

def main():
	openSite(domains)	

if __name__=="__main__":
	main()



		
