from mcp_client import MCPClient

class DifyAgentPlugin:
    def __init__(self, mcp_server_url):
        self.mcp_client = MCPClient(mcp_server_url)

    def call_function(self, function_name, parameters):
        if function_name == "mcp_call":
            return self.mcp_client.send_request(parameters)
        else:
            # 处理普通函数调用
            return self._call_normal_function(function_name, parameters)

    def _call_normal_function(self, function_name, parameters):
        # 这里可以添加普通函数调用的逻辑
        print(f"Calling normal function: {function_name} with parameters: {parameters}")
        return {"result": f"Function {function_name} called successfully"}