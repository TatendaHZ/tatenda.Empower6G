import websocket
import json
import base64

# WebSocket URL (replace with your WebUI websocket URL)
ws_url = "ws://192.168.2.8:30080/"

# Your credentials
username = "admin"
password = "1423"

# Encode credentials for basic auth if required
auth_header = "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()

def on_message(ws, message):
    data = json.loads(message)
    # Example: subscriber info is usually under 'subscribers' key
    if "subscribers" in data:
        for sub in data["subscribers"]:
            print(f"IMSI: {sub.get('imsi')}, MSISDN: {sub.get('msisdn')}, Name: {sub.get('name')}")

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

def on_open(ws):
    print("WebSocket opened")
    # Request all subscribers (the exact payload depends on Open5GS WebUI implementation)
    request_payload = json.dumps({
        "type": "subscribe",  # or "get_subscribers" depending on WebUI
        "resource": "subscribers"
    })
    ws.send(request_payload)

if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        ws_url,
        header=[f"Authorization: {auth_header}"],
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()

