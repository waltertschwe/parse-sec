import os
import requests
import time
import xml.etree.ElementTree as etree

class XmlHandler():

	def __init__(self, count = "50"):
		self.sec_atom_feed = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=&company=&dateb=&owner=include&start=0&count=" + count + "&output=atom"
		self.sec_data_file = "../data/sec-data-" + time.strftime("%Y%m%d-%H%M%S") + ".xml"

	def curlFeed(self):
		r = requests.get(self.sec_atom_feed)
		if r.status_code == 200:
			## save data to local file system
			dataFile = open(self.sec_data_file,'w')
			dataFile.write(r.text)
			
			## parse ATOM feed
			root = etree.fromstring(r.text)
			entries = root.findall('{http://www.w3.org/2005/Atom}entry') 
			for entries in root:
				for entry in entries:
					if (entry.tag == "{http://www.w3.org/2005/Atom}title"):
						print(entry.text)
					
					print(entry.tag, entry.attrib)
