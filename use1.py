import requests
from cisco_support.bug import Bug

# Set your API key and secret
key = '6h9p6ysfjd33ef5byynqddr4'
secret = 'tW6x5HMPQHV84ZtwceKBeUUt'

# Create an instance of the Bug class with your credentials
bug_instance = Bug(key, secret)

# Call the method to retrieve the access token
token = bug_instance._Bug__headers['Authorization'].split(' ')[1]

# Print the authorization token
print(f"Authorization Token: {token}")
