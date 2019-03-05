from time import sleep
import requests
from bs4 import BeautifulSoup as Soup

# url='https://en.wikipedia.org/wiki/Agent_Orange'
# url = 'http://img2.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5IqcltAYXIsYFSKhOGuLuTuIa3UIaPtIuTwIa3X7bVJCfdNhFVXLRXUM5SqMRYqAS.AV8tO2YtQV8tQ46XsMOGuhK&time=201902131250&inya=true'
url = 'http://img1.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5IqcltAYXIs8FGl48TuIa3UIaPtIuTXIaYw7bVJCfdNhFVXLRXUM5SqMRYqAS.AV8tO2YtQV8tch3XsMOGuCRUB&time=201902131520&inya=true'

# html = Soup(requests.get(url).text, features="lxml")
# html = requests.get(url, stream=True)
html = requests.get(url)
data = html.text
print(f"Image size: {len(data)} bytes")

# image_links = [(url + a['href'])
#                for a in html.find_all('a', {'class': 'image'})]

# for img_url in image_links:
#     response = requests.get(img_url)
#     try:
#         print(
#             f"Size of image {img_url} = {response.headers['Content-Length']} bytes")
#     except KeyError:
#         print(f"Server didn't specify content length in headers for {img_url}")
#     sleep(0.5)
