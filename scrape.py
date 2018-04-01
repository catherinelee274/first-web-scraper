from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
html = urlopen(url)

soup = BeautifulSoup(html, "html5lib")
table = soup.find('tbody', attrs = {'class': 'stripe'}) #all inmate names are under <tbody>

row_info = []
for row in table.findAll('tr')[1:]: #[1:] is to skip the first row so we can write our own headers
    cell_info = []
    for cell in row.findAll('td'):
        text = cell.text.replace('\n\xa0Details\n','')
        cell_info.append(text)
    row_info.append(cell_info)

outfile = open("./inmates.csv","w") #w over wb because wb is for writing in binary mode. use 'w' for normal text files 
writer = csv.writer(outfile)
writer.writerow(["Last","First","Middle","Gender","Race","Age","City","State"])
writer.writerows(row_info)

#CLOSE IS IMPORTANT, doesn't write anything to the csv file if you don't use it
outfile.close()


 

