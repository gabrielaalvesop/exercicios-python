import urllib.request
import urllib

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print("o site pudim não está acessível no momento!")
else:
    print("Consegui acessar o site pudim!")
