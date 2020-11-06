
from bs4 import BeautifulSoup
import requests
from operator import itemgetter

myDatastr = ''
cases_of_india = ''
cases_of_us = ''
cases_of_brazil = ''
cases_of_russia = ''
cases_of_colombia = ''
cases_of_peru = ''
cases = []

def getData(url):
    data = requests.get(url)
    return data.text

def ToInt(s):
    s = s.split(',')
    s = int(''.join(s))
    return s

r = getData('https://www.worldometers.info/coronavirus/#countries')
soup = BeautifulSoup(r,'html.parser')

for tr in soup.find_all('tbody'):
    myDatastr += tr.get_text()
myDatastr = myDatastr[1:]
itemlist =  myDatastr.split('\n\n\n')


for item in itemlist[38:44]:
##    print(item.split('\n'))
    cases.append(item.split('\n'))

cases_of_us = cases[0][3]
cases_of_india = cases[1][2]
cases_of_brazil = cases[2][2]
cases_of_russia = cases[3][2]
cases_of_colombia = cases[4][2]
cases_of_peru = cases[5][2]

cases_of_us = ToInt(cases_of_us)
cases_of_india = ToInt(cases_of_india)
cases_of_brazil = ToInt(cases_of_brazil)
cases_of_russia = ToInt(cases_of_russia)
cases_of_colombia = ToInt(cases_of_colombia)
cases_of_peru = ToInt(cases_of_peru)



from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')


plt.title('COVID CASES SCATTER GRAPH')
plt.ylabel('cases per million')


plt.scatter(0,cases_of_us,label = 'cases of US')
plt.scatter(2,cases_of_india,label = 'cases of IND')
plt.scatter(4,cases_of_brazil,label = 'cases of BRAZIL')
plt.scatter(6,cases_of_russia,label = 'cases of RUSSIA')
plt.scatter(8,cases_of_colombia,label = 'cases of COLOMBIA')
plt.scatter(10,cases_of_peru,label = 'cases of PERU')


plt.legend()
plt.show()