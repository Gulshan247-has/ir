import csv
import requests
import xml.etree.ElementTree as ET

def loadRSS():
    url = "https://www.hindustantimes.com/feeds/rss/sports/football/rssfeed.xml"
    resp = requests.get(url)
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)

def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    newsitems = []
    for item in root.findall('./channel/item'):
        news = {}
        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')

        newsitems.append(news)
    return newsitems
def savetocsv(newsitems, filename):
    #field for csv file
    fields=['guid', 'tile', 'desciption', 'ink', 'media']

    #write to csv file
    with open (filename,'w') as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames = fields)
        #write header fieldname
        writer.writeheader()
        #writering data rows
        writer.writerows(newsitems)

def main():
#load rss from web to update  exiting xml file
    loadRSS()
    newsitems = parseXML('topnewsfeed.xml')
    savetocsv(newsitems, 'topnews.csv')
    
if __name__=="__main__":
    main()
 
