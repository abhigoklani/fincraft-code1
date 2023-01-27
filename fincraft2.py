import requests
from bs4 import BeautifulSoup
import pandas as pd

gst_mapping =pd.read_csv("gst_mapping.csv")

def extract_product_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    products= soup.find_all('div' , class_ = 'products')
    product_list = []
    for product in products:
        name = product.find('div' , class_ = 'product_name').get_text()
        category = product.find('div', class_ = 'product_category').get_text()
        price = product.find('div', class_ = 'product_price').get_text()

        gst_rate=gst_mapping[gst_mapping['category'] == category]['GST Rate'].valurs[0]
        product_list.append({'Name': name, 'category': category, 'price': price, 'GST Rates': gst_rate})
        return product_list
website1_url = "https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=58075519359&hvpone=&hvptwo=&hvadid=610780881833&hvpos=&hvnetw=g&hvrand=9068498349830648903&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9299054&hvtargid=kwd-64107830&hydadcr=14452_2316413&gclid=Cj0KCQiAic6eBhCoARIsANlox85aCbZYHl4vv5pfF3iQdWlKkgrdLlMYMvKf3golkGKuJzEhVBTn1nUaAmYOEALw_wcB"
website2_url = "https://www.flipkart.com/"
product_list1= extract_product_info(website1_url)
product2_list=extract_product_info(website2_url)
product_list= product_list1 + product2_list
df=pd.DataFrame(product_list)
df['price']= df['price'].str.replace(',','').astype(float)
print("Average GST rate by product category: ")
print(df.groupby('category')['GST Rate'].mean())
print("total sales by category: ")
print(df.groupby('category')['price'].sum())
df=df.head(50)
df.to_csv("product_list.csv",index = False)