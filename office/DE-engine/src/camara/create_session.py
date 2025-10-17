import requests
import json
import os

# === API Configuration ===
API_ROOT = "http://192.168.88.36:30991/"
BASE_PATH = "qod/v0"
SESSIONS_ENDPOINT = f"{API_ROOT}{BASE_PATH}/sessions"

# === Payload for creating a QoS session ===
payload = {
    "duration": 86400,
    "ueId": {"ipv4addr": "10.45.0.2"},   # You can change this
    "asId": {"ipv4addr": "192.168.88.40"},  # You can change this
    "uePorts": {"ranges": [{"from": 0, "to": 65535}]},
    "asPorts": {"ranges": [{"from": 0, "to": 65535}]},
    "qos": "QOS_O",
    "notificationUri": "http://192.168.88.36:30991/notifications",
    "notificationAuthToken": "c8974e592c2fa383d4a3960714"
}

# === Headers for the request ===
headers = {
    "Content-Type": "application/json"
}

SESSION_FILE = "session_info.txt"

def load_sessions():
    """Load sessions from file into a list of dicts."""
    if not os.path.exists(SESSION_FILE):
        return []
    with open(SESSION_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_sessions(sessions):
    """Save sessions list to file as JSON."""
    with open(SESSION_FILE, "w") as f:
        json.dump(sessions, f, indent=2)

def create_session():
    try:
        response = requests.post(SESSIONS_ENDPOINT, json=payload, headers=headers)

        if response.status_code == 201:
            data = response.json()
            print("✅ Session created successfully!")
            print("Response:", json.dumps(data, indent=2))

            ue_ip = data.get("ueId", {}).get("ipv4addr")
            as_ip = data.get("asId", {}).get("ipv4addr")
            session_id = data.get("id")
            qos = data.get("qos")

            # Load existing sessions
            sessions = load_sessions()

            # Check if UE and AS combination already exists
            existing_index = next((i for i, s in enumerate(sessions)
                                   if s["UE ID"] == ue_ip and s["AS ID"] == as_ip), None)

            session_entry = {
                "UE ID": ue_ip,
                "AS ID": as_ip,
                "Session ID": session_id,
                "QoS": qos
            }

            if existing_index is not None:
                # Replace existing entry
                sessions[existing_index] = session_entry
                print(f"♻️  Updated existing session for UE {ue_ip} and AS {as_ip}")
            else:
                # Append new entry
                sessions.append(session_entry)
                print(f"➕ Added new session for UE {ue_ip} and AS {as_ip}")

            # Save updated sessions
            save_sessions(sessions)
            print(f"📄 Session information stored in {SESSION_FILE}")

        else:
            print(f"❌ Failed to create session. Status code: {response.status_code}")
            print("Response:", response.text)

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error occurred while making the request: {e}")

if __name__ == "__main__":
    create_session()
