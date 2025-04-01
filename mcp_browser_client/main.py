from dify_plugin import Plugin, DifyPluginEnv
from dify_agent_plugin import DifyAgentPlugin

plugin = Plugin(DifyPluginEnv(MAX_REQUEST_TIMEOUT=120))

# 初始化插件
mcp_server_url = "http://localhost:8000"
plugin = DifyAgentPlugin(mcp_server_url)

# 调用MCP工具
mcp_parameters = {"key": "value"}
mcp_result = plugin.call_function("mcp_call", mcp_parameters)
print(f"MCP call result: {mcp_result}")

# 调用普通函数
normal_parameters = {"param1": "test"}
normal_result = plugin.call_function("normal_function", normal_parameters)
print(f"Normal function call result: {normal_result}")

if __name__ == '__main__':
    plugin.run()
