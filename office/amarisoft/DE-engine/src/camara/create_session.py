import requests
import json

# API configuration
API_ROOT = "http://192.168.3.89:30991/"
BASE_PATH = "qod/v0"
SESSIONS_ENDPOINT = f"{API_ROOT}{BASE_PATH}/sessions"

# Payload for creating a QoS session
payload = {
    "duration": 86400,
    "ueId": {
        "ipv4addr": "10.45.0.2"
    },
    "asId": {
        "ipv4addr": "192.168.3.108"
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
    "qos": "QOS_M",
    "notificationUri": "http://192.168.3.89:30991/notifications",
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
        data = response.json()
        print("Session created successfully!")
        print("Response:", json.dumps(data, indent=2))

        # Extract UE IP and session ID
        ue_ip = data.get("ueId", {}).get("ipv4addr")
        session_id = data.get("id")

        # Save them to a file
        with open("session_info.txt", "w") as f:
            f.write(f"UE IP: {ue_ip}\n")
            f.write(f"Session ID: {session_id}\n")

        print(f"UE IP and Session ID saved to session_info.txt")

    else:
        print(f"Failed to create session. Status code: {response.status_code}")
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print(f"Error occurred while making the request: {e}")
