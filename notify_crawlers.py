import requests
import sys

SITE_URL = "https://siddharth-maddali.github.io"
SITEMAP_URL = f"{SITE_URL}/sitemap.xml"
INDEXNOW_KEY = "97c55866164f43399434863920260129"
INDEXNOW_KEY_LOCATION = f"{SITE_URL}/{INDEXNOW_KEY}.txt"

def notify_indexnow():
    """Notifies Bing and Yandex via IndexNow."""
    url = "https://api.indexnow.org/indexnow"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {
        "host": "siddharth-maddali.github.io",
        "key": INDEXNOW_KEY,
        "keyLocation": INDEXNOW_KEY_LOCATION,
        "urlList": [
            SITE_URL,
            f"{SITE_URL}/blog.html",
            f"{SITE_URL}/professional/cv",
            f"{SITE_URL}/professional/resume"
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in [200, 202]:
            print("Successfully notified IndexNow (Bing, Yandex).")
        else:
            print(f"IndexNow notification failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error notifying IndexNow: {e}")

if __name__ == "__main__":
    print("Notifying crawlers...")
    # Google and Bing Legacy sitemap pings are deprecated (404/410).
    # Google now relies solely on robots.txt (Sitemap directive) and Search Console.
    notify_indexnow()
    print("Done.")