import requests
import json
import urllib3
import base64
# Claudi 20250408
# Disable SSL warnings (for self-signed certificates)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# PowerScale connection details
CLUSTER_IP = "192.168.55.62"
USERNAME = "admin"
PASSWORD = "password"
API_ENDPOINT = f"https://{CLUSTER_IP}:8080"  # Default HTTPS port for PowerScale REST API

# Target directory to delete
TARGET_DIR = "/ifs/py"

def delete_directory():
    """Delete the target directory and all its contents using the REST API"""
    
    # Use the PAPI (Platform API) endpoint to delete the directory
    delete_url = f"{API_ENDPOINT}/namespace{TARGET_DIR}"
    
    # Create headers with Basic Authentication
    auth_string = f"{USERNAME}:{PASSWORD}"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()
    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "Content-Type": "application/json"
    }
    
    # Parameters for recursive deletion
    params = {
        "recursive": "true"
    }
    
    try:
        print(f"Sending DELETE request to: {delete_url}")
        response = requests.delete(delete_url, headers=headers, params=params, verify=False)
        response.raise_for_status()
        print(f"Successfully deleted directory: {TARGET_DIR}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to delete directory: {e}")
        if hasattr(e, 'response') and e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response text: {e.response.text}")
        return False

def main():
    """Main function to delete the directory"""
    print(f"Connecting to PowerScale cluster at {CLUSTER_IP}...")
    
    # Delete the directory using basic auth instead of sessions
    print(f"Attempting to delete directory: {TARGET_DIR}")
    result = delete_directory()
    
    if result:
        print("Directory deletion completed successfully.")
    else:
        print("Directory deletion failed.")

if __name__ == "__main__":
    main()