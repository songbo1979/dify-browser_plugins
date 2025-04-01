import requests

class MCPClient:
    def __init__(self, server_url):
        self.server_url = server_url

    def send_request(self, data):
        try:
            response = requests.post(self.server_url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error sending request to MCP server: {e}")
            return None