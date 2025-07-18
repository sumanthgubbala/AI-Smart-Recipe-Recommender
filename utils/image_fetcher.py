import requests

PEXELS_API_KEY = "ohAr5yIEeSMi32jh9UQpjBWKZFHuqcmoC8AjvdGhFVoFHHzfed76rL7S"  # 🔐 Replace with your actual API key

def fetch_image_url(query):
    url = "https://api.pexels.com/v1/search"
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    params = {
        "query": query,
        "per_page": 1
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['photos']:
            return data['photos'][0]['src']['medium']
    return None
