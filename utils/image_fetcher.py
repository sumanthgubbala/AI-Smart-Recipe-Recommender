import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, unquote




def get_image_by_class(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            # Look for img tag with both class names
            image_tag = soup.find("img", class_="rounded-3xl object-cover")

            # If not found due to multiple class matching, use CSS selector
            if not image_tag:
                image_tag = soup.select_one("img.rounded-3xl.object-cover")

            src = image_tag.get("src")
            if src.startswith("/_next/image"):
                parsed = urlparse(src)
                query = parse_qs(parsed.query)
                actual_url = query.get("url", [None])[0]
                if actual_url:
                    return unquote(actual_url)
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None