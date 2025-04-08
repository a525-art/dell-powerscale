import requests
import json
import urllib3
import base64
import sys

# Disable SSL warnings (for self-signed certificates)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# PowerScale connection details
CLUSTER_IP = "192.168.55.62"
USERNAME = "admin"
PASSWORD = "password"
API_ENDPOINT = f"https://{CLUSTER_IP}:8080"  # Default HTTPS port for PowerScale REST API

# Target directory to delete
TARGET_DIR = "/ifs/py"

def get_basic_auth_header():
    """Generate the Basic Authentication header"""
    auth_string = f"{USERNAME}:{PASSWORD}"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()
    return {"Authorization": f"Basic {encoded_auth}", "Content-Type": "application/json"}

def check_directory_exists():
    """Check if the target directory exists"""
    check_url = f"{API_ENDPOINT}/namespace{TARGET_DIR}"
    
    try:
        response = requests.get(
            check_url, 
            headers=get_basic_auth_header(), 
            verify=False
        )
        
        # If status code is 200, directory exists
        if response.status_code == 200:
            print(f"Directory {TARGET_DIR} exists.")
            return True
        else:
            print(f"Directory {TARGET_DIR} does not exist. Status code: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and e.response:
            if e.response.status_code == 404:
                print(f"Directory {TARGET_DIR} does not exist.")
                return False
            else:
                print(f"Error checking directory: {e}")
                print(f"Response status code: {e.response.status_code}")
                print(f"Response text: {e.response.text}")
                return False
        else:
            print(f"Connection error while checking directory: {e}")
            return False

def delete_directory():
    """Delete the target directory and all its contents using the REST API"""
    delete_url = f"{API_ENDPOINT}/namespace{TARGET_DIR}"
    
    # Parameters for recursive deletion
    params = {
        "recursive": "true"
    }
    
    try:
        print(f"Sending DELETE request to: {delete_url}")
        response = requests.delete(
            delete_url, 
            headers=get_basic_auth_header(), 
            params=params, 
            verify=False
        )
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
    """Main function to check and delete the directory"""
    print(f"Connecting to PowerScale cluster at {CLUSTER_IP}...")
    
    # First check if directory exists
    print(f"Checking if directory exists: {TARGET_DIR}")
    if not check_directory_exists():
        print("Directory doesn't exist or cannot be accessed. Exiting.")
        sys.exit(1)
    
    # If we get here, the directory exists, so delete it
    print(f"Attempting to delete directory: {TARGET_DIR}")
    result = delete_directory()
    
    if result:
        print("Directory deletion completed successfully.")
    else:
        print("Directory deletion failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()