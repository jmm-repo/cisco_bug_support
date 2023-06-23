from cisco_support import Bug
from cisco_support.utils import getToken

# Your client_id and client_secret
client_id = '6h9p6ysfjd33ef5byynqddr4'
client_secret = 'tW6x5HMPQHV84ZtwceKBeUUt'

# Get the access token
access_token = getToken(client_id, client_secret,proxies=None,verify=True)

# Create a Bug object
bug = Bug(access_token)

# Now you can use the methods of the Bug class to interact with the Cisco API
# For example, to get information about a list of bugs
bug_ids = ['CSCvd78303', 'CSCvd78304']  # replace with your bug IDs
bug_info = bug.getBugIDs(bug_ids)

# Print the bug information
print(bug_info)

