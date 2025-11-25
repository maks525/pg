import sys
import requests
import re

def download_url_and_get_all_hrefs(url):

    hrefs = []
    response = requests.get(url)
    if response.status_code != 200:
        return hrefs 

    html = response.text
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)

    return hrefs

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        for h in hrefs:
            print(h)
    
    except Exception as e:
        print(f"Program skoncil chybou: {e}")