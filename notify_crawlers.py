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

def notify_google():
    """Pings Google Sitemap (Legacy)."""
    # Note: Google deprecated the ping endpoint in Dec 2023, but it's harmless and sometimes still logged.
    # The 'best' way for Google is really just ensuring sitemap.xml is in robots.txt (which it is).
    ping_url = f"https://www.google.com/ping?sitemap={SITEMAP_URL}"
    try:
        response = requests.get(ping_url)
        if response.status_code == 200:
            print("Successfully pinged Google Sitemap.")
        else:
            print(f"Google Sitemap ping failed: {response.status_code}")
    except Exception as e:
        print(f"Error pinging Google: {e}")

def notify_bing_legacy():
    """Pings Bing Sitemap (Legacy)."""
    ping_url = f"https://www.bing.com/ping?sitemap={SITEMAP_URL}"
    try:
        response = requests.get(ping_url)
        if response.status_code == 200:
            print("Successfully pinged Bing Sitemap.")
        else:
            print(f"Bing Sitemap ping failed: {response.status_code}")
    except Exception as e:
        print(f"Error pinging Bing: {e}")

if __name__ == "__main__":
    print("Notifying crawlers...")
    notify_indexnow()
    notify_google()
    notify_bing_legacy()
    print("Done.")
