import requests

def get_token(client_id, client_secret):
    url = "https://cloudsso.cisco.com/as/token.oauth2"
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        print(f"Failed to get access token. Status code: {response.status_code}, Response: {response.text}")
        return None

client_id = "6h9p6ysfjd33ef5byynqddr4"  # replace with your client id
client_secret = "tW6x5HMPQHV84ZtwceKBeUUt"  # replace with your client secret

token = get_token(client_id, client_secret)
if token:
    print(f"Access token: {token}")

