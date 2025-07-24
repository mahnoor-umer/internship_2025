## Web scrapping

""" 

https://www.python.org/blogs/

https://cran.r-project.org/

https://posit.co/download/rstudio-desktop/

"""

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.python.org/blogs/",
    "https://cran.r-project.org/",
    "https://posit.co/download/rstudio-desktop/"
]

def fetch_content(url):
    response= requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print( f"This web page has a length of {len(soup.text)} words")

threads = [] 

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()


# Wait for all threads to finish
for thread in threads:
    thread.join()

print( f"Web pages have been successfully fetched")