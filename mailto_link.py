import requests
from bs4 import BeautifulSoup



emailList= []

#add url of the page you want to scrape to urlString
#urlString='https://www.prosweets.com/exhibitors-and-products/exhibitor-index/?fw_goto=aussteller/details&&kid=0002210598'
#urlString='https://www.imm-cologne.com/exhibitor/kroencke'
urlString='https://exhibitorlist4.fairdesigner.de/v1.4/catalog/A000016531?tenantnr=10124&tenant=Euroexpo&eventid=0762022&language=en&page=1&entries_per_page=10&custom_css'


#function that extracts all emails from a page you provided and stores them in a list
def emailExtractor(urlString):
    getH=requests.get(urlString)
    h=getH.content
    soup=BeautifulSoup(h,'html.parser')
    title=soup.title.text.strip()
    print(title)
    mailtos = soup.select('a[href^=mailto]')
    for i in mailtos:
        href=i['href']
        try:
            str1, str2 = href.split(':')
        except ValueError:
            break
        
        emailList.append(str2)
        print(str2)
        
        
            

emailExtractor(urlString)