import requests

# Define your Client ID and Client Secret
client_id = '6h9p6ysfjd33ef5byynqddr4'
client_secret = 'tW6x5HMPQHV84ZtwceKBeUUt'

# Define the authentication endpoint URL
auth_url = 'https://cloudsso.cisco.com/as/token.oauth2'

# Define the request parameters
params = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

# Send the authentication request
response = requests.post(auth_url, data=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()

    # Extract the access token
    access_token = data['access_token']

    # Print the access token
    print(f"Access Token: {access_token}")
else:
    print(f"Authentication request failed with status code {response.status_code}")

