import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "-q", "install", package])

#pass the module you want installed as a string and then import! (No GUI support)
install('requests')

import socket
import requests

hostname = socket.gethostname()

r = requests.get('https://get.geojs.io/')

ipreq = requests.get('https://get.geojs.io/v1/ip.json')
ipadd = ipreq.json()['ip']

url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
geo = requests.get(url)
geodata = geo.json()