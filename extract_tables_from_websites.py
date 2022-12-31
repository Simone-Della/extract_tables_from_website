# Import libraries
import ssl
import pandas as pd

#to bypass ssl verify certification
ssl._create_default_https_context = ssl._create_unverified_context

#url to extract tables
url = 'https://it.wikipedia.org/wiki/Statistiche_di_Formula_1'

table = pd.read_html(url, attrs = {'class': 'wikitable'}) 
len(table)

count = 0
#create in file tables.xlx create a sheet for each tables in url
with pd.ExcelWriter("tables.xlsx") as writer:
    for tables in table:
        count = count + 1 
        tables.to_excel(writer, sheet_name= 'sheet' + str(count))


