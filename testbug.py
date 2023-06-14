import json
from cisco_support import Bug

# Your API keys
client_key = 'your_client_key'
client_secret = 'your_client_secret'

# Initialize the Bug API
bugs = Bug(client_key, client_secret)

# List of platform/release combinations
platform_release_combinations = [
    ('WS-C3560-48PS-S', '12.2(25)SE'),
    # Add more combinations here
]

# Loop through the combinations and get the bugs
for platform, release in platform_release_combinations:
    bug_data = bugs.getByBaseProductIDsAndSoftwareReleases(platform, release, modified_date=5, sort_by='modified_date')
    print(json.dumps(bug_data, indent=4))
