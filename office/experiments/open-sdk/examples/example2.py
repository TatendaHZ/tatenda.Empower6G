# from sunrise6g_opensdk import Sdk as sdkclient # For PyPI users
from sunrise6g_opensdk.common.sdk import Sdk as sdkclient  # For developers


def main():
    # Only specify the network adapter for Open5GS/NEF
    adapter_specs = {
        "network": {
            "client_name": "open5gs",
            "base_url": "http://10.101.30.223:80",
            "scs_as_id": "id_example",  # Replace with your actual SCS/AS ID
        },
    }

    adapters = sdkclient.create_adapters_from(adapter_specs)
    network_client = adapters.get("network")

    print("Network client ready to be used:", network_client)

    # Example NEF calls
    # Uncomment and replace with actual session IDs or data
    # print("Testing network client function: 'get_qod_session'")
    # response = network_client.get_qod_session(session_id="example_session_id")
    # print(response)
    

if __name__ == "__main__":
    main()
