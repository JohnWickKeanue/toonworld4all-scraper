import time
from bs4 import BeautifulSoup
import requests
from requests import get
url = "https://toonworld4all.me/redirect/main.php?url=KSwycP1PDamlOYL0VQUP1CqnUdX4OLLzzxF6t9X+kWMlKRyuTSUvQrvLSTptpu6jjslzSjFOSbWhPW94HeXbUw=="

def flix(url):
      client = requests.session()
      download = get(url, stream=True, allow_redirects=False)
      v = download.headers["location"]
      DOMAIN = "https://share.techymedies.com"
      code = v.split("/")[-1]
      final_url = f"{DOMAIN}/{code}"
      ref = "https://disheye.com/"
      h = {"referer": ref}
      resp = client.get(final_url, headers=h)
      soup = BeautifulSoup(resp.content, "html.parser")
      inputs = soup.find(id="go-link").find_all(name="input")
      data = { input.get('name'): input.get('value') for input in inputs }
      h = { "x-requested-with": "XMLHttpRequest" }
      time.sleep(5)
      r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
      return r.json()['url']
                     
print(flix(url))
