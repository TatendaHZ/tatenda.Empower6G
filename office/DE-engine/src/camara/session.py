import requests
import json

# API configuration
API_ROOT = "http://192.168.88.40:30991/"
BASE_PATH = "qod/v0"
SESSIONS_ENDPOINT = f"{API_ROOT}{BASE_PATH}/sessions"

# Payload for creating a QoS session
payload = {
    "duration": 86400,
    "ueId": {
        "ipv4addr": "10.45.0.2"
    },
    "asId": {
        "ipv4addr": "192.168.88.38"
    },
    "uePorts": {
        "ranges": [
            {
                "from": 0,
                "to": 65535
            }
        ]
    },
    "asPorts": {
        "ranges": [
            {
                "from": 0,
                "to": 65535
            }
        ]
    },
    "qos": "QOS_S",
    "notificationUri": "http://192.168.88.40:30991/notifications",
    "notificationAuthToken": "c8974e592c2fa383d4a3960714"
}

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

try:
    # Send POST request to create a session
    response = requests.post(SESSIONS_ENDPOINT, json=payload, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 201:
        print("Session created successfully!")
        print("Response:", json.dumps(response.json(), indent=2))
    else:
        print(f"Failed to create session. Status code: {response.status_code}")
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print(f"Error occurred while making the request: {e}")
