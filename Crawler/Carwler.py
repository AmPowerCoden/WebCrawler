import requests
import re
from bs4 import BeautifulSoup

if __name__ == "__main__":
    URL = "https://de.wikipedia.org/wiki/Astronomische_Koordinatensysteme#Relative_Koordinatensysteme"
    resp = requests.get(URL)
    print(resp.status_code)
    print(resp.text)
    soup = BeautifulSoup(resp.text)

    x = soup.findAll('a', attrs={'href': re.compile("^http://")})

    regex_pattern = r'\s+<a href="(.*?)"'

    print(re.findall(regex_pattern, resp.text))

    regex = re.findall