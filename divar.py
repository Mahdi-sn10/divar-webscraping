from bs4 import BeautifulSoup
import re
import requests
import arabic_reshaper
from bidi.algorithm import get_display
url_page=requests.get('https://divar.ir/s/kerman')
soup=BeautifulSoup(url_page.text,'html.parser')
l= soup.find_all('div',class_='kt-post-card__body')
esm_kala=list()
gheymat_kala=list()
a=dict()
for item in l:
    e=item.text
    reshaped_text = arabic_reshaper.reshape(e)    # correct its shape
    e = get_display(reshaped_text)

    k=re.search(r"ﯼﺭﻮﻓ",e)
    if  k!=None:
        print(e)

