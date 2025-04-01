from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

def generate_private_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key

def save_private_key(private_key, filename):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(filename, 'wb') as f:
        f.write(pem)

def load_private_key(filename):
    with open(filename, 'rb') as f:
        pem = f.read()
    private_key = serialization.load_pem_private_key(
        pem,
        password=None,
        backend=default_backend()
    )
    return private_key

def sign_file(private_key, file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def save_signature(signature, filename):
    with open(filename, 'wb') as f:
        f.write(signature)

if __name__ == "__main__":
    # 生成私钥
    private_key = generate_private_key()
    save_private_key(private_key, 'private_key.pem')

    # 加载私钥
    private_key = load_private_key('private_key.pem')

    # 要签名的文件
    difypkg_file = 'dify_mcp_plugin.difypkg'

    # 生成签名
    signature = sign_file(private_key, difypkg_file)

    # 保存签名
    save_signature(signature, 'dify_mcp_plugin.difypkg.signature')