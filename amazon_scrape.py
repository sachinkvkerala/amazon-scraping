import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

url="https://www.amazon.com/VIZIO-Chromecast-Mirroring-Streaming-Channels/dp/B092Q1TRJC"

response=requests.get(url,HEADERS)

content=response.content

soup = BeautifulSoup(content, "lxml")

title = soup.find("span", attrs={"id":'productTitle'}).string.strip()

additional = soup.find("table", attrs={"class":'a-normal a-spacing-micro'})


data = {}
for row in additional.find_all("tr"):
    key_element, value_element = row.find_all("td")
    key = key_element.text.strip()
    value = value_element.text.strip()
    data[key] = value

print(data)

price = soup.find("span", attrs={"class":'a-price-whole'}).text


discount = soup.find("div", attrs={"class":'a-section a-spacing-none aok-align-center aok-relative'})


try:
    price=soup.find("span",{"class":"a-price"}).find("span").text
except:
    price=None
    
    
price = soup.find('span', attrs={'class':'p13n-sc-price'})


price = soup.find("span", attrs={'id': 'taxInclusiveMessage'})

price = soup.find('span', {'id':"taxInclusiveMessage"})
print(price)


span_element = soup.find('span', class_='aok-offscreen')


span_element = soup.select_one('#corePriceDisplay_desktop_feature_div > div > span.aok-offscreen')


span_element = soup.select_one('/html/body/div[4]/div/div[11]/div[5]/div[4]/div[15]/div/div/div[1]/div/div[3]/div[1]/span[3]/span[2]/span[2]')

span_element = soup.select_one('body > div:nth-child(4) > div > div:nth-child(11) > div:nth-child(5) > div:nth-child(4) > div:nth-child(15) > div > div > div:nth-child(1) > div > div:nth-child(3) > div:nth-child(1) > span:nth-child(3) > span:nth-child(2) > span:nth-child(2)')


span_element = soup.select_one('span.a-price-whole')
