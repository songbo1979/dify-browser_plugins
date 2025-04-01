from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

def sign_plugin(plugin_file_path, private_key_path):
    # 读取私钥
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    # 读取插件文件内容
    with open(plugin_file_path, "rb") as plugin_file:
        plugin_content = plugin_file.read()
    # 进行签名
    signature = private_key.sign(
        plugin_content,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    # 保存签名文件
    signature_file_path = os.path.splitext(plugin_file_path)[0] + ".sig"
    with open(signature_file_path, "wb") as signature_file:
        signature_file.write(signature)
    print(f"Signature saved to {signature_file_path}")

if __name__ == "__main__":
    plugin_file_path = "dify_mcp_plugin.difypkg"
    # 修改为实际的私钥文件路径
    private_key_path = "E:/Dify/mcp_browser_client/private_key.pem"
    sign_plugin(plugin_file_path, private_key_path)