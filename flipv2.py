from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
NAME = []
PRICE = []
RATING = []
IMAGE = []
headers = {"User-Agent":
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}


for page in range(1,21):
    print(f"Scraping page {page}...")
    url = f"https://www.flipkart.com/search?q=mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile%7CMobiles&requestId=835ac98e-cb4a-43c5-8cb6-765e8a9ece59&as-searchtext=mobi&page={page}"
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content,"html.parser")
    soup.prettify()

    block = soup.select("a.CGtC98")
    # print(block)
    for data in block:
        name = data.select_one(".KzDlHZ")
    # print(name)
        price = data.select_one("._4b5DiR")
    # print(price)
        rating = data.select_one(".XQDdHH").text
    # print(rating)
        image = data.select_one("img.DByuf4").get('src')
    # print(image)
        NAME.append(name.text.strip())
    # print(NAME)
        PRICE.append(price.text.strip())
    # print(PRICE)
        RATING.append(rating.strip())
    # print(RATING)
        IMAGE.append(image)
    time.sleep(3) 
    # print(IMAGE)

   
data = {
        'NAMES':NAME,
        'PRICES':PRICE,
        'RATINGS':RATING,
        'IMAGES':IMAGE
    }

    # print(data)

df = pd.DataFrame(data)

    # print(df)
df.to_csv("flipv2.csv",index=False,encoding="utf8")
    




