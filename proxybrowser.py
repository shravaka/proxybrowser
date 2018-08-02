
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.webdriver import FirefoxProfile

domains = "domains1.txt"
myProxy = "192.168.64.175:3128"


def openSite(filename):

	profile = FirefoxProfile("/home/squid/proxyprofile/")
#	profile = webdriver.FirefoxProfile()
#	profile.set_preference("network.proxy.type",1)
#	profile.set_preference("network.proxy.http", "192.168.64.176")
#	profile.set_preference("network.proxy.http_port", 3128)
#	profile.set_preference("network.proxy.ssl", "192.168.64.176")
#	profile.set_preference("network.proxy.ssl_port", 3128)
#	profile.update_preferences()
	
	driver = webdriver.Firefox(firefox_profile=profile)
	with open (filename) as f:
		address = f.readline()
		while address:
			driver.get(address)
			address = f.readline()
	driver.close()

def main():
	openSite(domains)	

if __name__=="__main__":
	main()

