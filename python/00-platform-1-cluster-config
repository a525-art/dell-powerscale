import requests
from requests.auth import HTTPBasicAuth
import json

# Define Isilon Cluster Information
base_url = "https://192.168.55.51:8080"  # Replace with your Isilon cluster IP
username = "admin"  # Replace with your username
password = "P@ssw0rd"  # Replace with your password

# Disable SSL certificate warnings (for self-signed certs, use only in development)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Set the API endpoint (example: get cluster info)
url = f"{base_url}/platform/1/cluster/config"
headers = {
    'Content-Type': 'application/json',
}

# Send the GET request with basic authentication
response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers, verify=False)

# Check the status code
if response.status_code == 200:
    # If the response is successful, print the response JSON
    print("Cluster Info:")
    print(json.dumps(response.json(), indent=4))
else:
    # If the response failed, print the error message
    print(f"Failed to connect to Isilon. Status code: {response.status_code}")
    print(f"Error: {response.text}")

##
