from xml_parser import XmlHandler 

## paramter count is string for URL
## minimum returned entries is 10
xml = XmlHandler("10")
xml.curlFeed()