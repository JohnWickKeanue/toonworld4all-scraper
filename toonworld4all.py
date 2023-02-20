import time
from bs4 import BeautifulSoup
import requests
from requests import get
url = "https://toonworld4all.me/teen-titans-trouble-in-tokyo-2006-bluray-multi-audio-hindi/"

def flix(url):
    client = requests.session()
    r = client.get(url).text
    soup = BeautifulSoup (r, "html.parser")
    for a in soup.find_all("a"):
                   c= a.get("href")
                   if "redirect/main.php?" in c:
                       download = get(c, stream=True, allow_redirects=False)
                       v = download.headers["location"]
                       client = cloudscraper.create_scraper(allow_brotli=False)
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
                       time.sleep(10)
                       r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
                       return r.json()['url']
                       if "gdtot" in g:
                           t = client.get(g).text
                           soupt = BeautifulSoup(t, "html.parser")
                           title = soupt.title
                           gd_txt = f"{(title.text).replace('GDToT | ' , '')}\n{g}\n\n"
                           print(gd_txt)

print(flix(url))
