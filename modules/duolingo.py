import json
import requests


def check_duolingo(email):
    url = "https://www.duolingo.com/2017-06-30/users"

    params = {
        'email': email
    }
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com",
        "Origin": "https://www.google.com"
    }

    try:
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            if not ('{"users":[]}' in response.text):
                return response.json()
        return False
    except Exception as e:
        print(e)
        return False
