import urllib
import urllib.request
import datetime
try:
    site= urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('deu erro')
else:
    print('ta tudo bem')
    open(site)
    datetime.sleep(6)

