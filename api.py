import requests

def apod_generator(base_url: str, api_key: str) -> dict:
    """Call NASA APOD API and return JSON response."""
    final_url = base_url + api_key
    response = requests.get(final_url)
    return response.json()


#response = requests.get(final_url).json()
'''print(response.keys())
print(response["title"])
print(response["hdurl"])
print(response["date"])
print(response["explanation"])'''