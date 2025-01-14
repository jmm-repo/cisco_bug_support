"""Script used to grab a token from cisco registered app"""
import requests
import yaml


URL = "https://cloudsso.cisco.com/as/token.oauth2"

with open("./credentials.yaml", encoding="utf-8") as file:
    myvars = yaml.safe_load(file)

payload = f"grant_type=client_credentials&client_id={myvars['6h9p6ysfjd33ef5byynqddr4']}&client_secret={myvars['tW6x5HMPQHV84ZtwceKBeUUt']}"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

response = requests.request("POST", URL, headers=headers, data=payload)

if response.status_code == 200:
    with open("credentials.yaml", encoding="utf-8") as f:
        creds = yaml.load(f, Loader=yaml.SafeLoader)

    creds["support_auth_token"] = response.json()["access_token"]

    # Rewriting credentials.yaml with new token variable
    with open("credentials.yaml", "w", encoding="utf-8") as f:
        yaml.dump(creds, f)
        print("Auth token updated successfully!!!")
else:
    print("Failed to update token, please check client ID or client secret")
