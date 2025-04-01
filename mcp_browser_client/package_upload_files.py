import zipfile
import os

def create_upload_zip(zip_name, file_paths):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in file_paths:
            if os.path.exists(file_path):
                arcname = os.path.basename(file_path)
                zipf.write(file_path, arcname)

if __name__ == "__main__":
    zip_name = "dify_plugin_upload.zip"
    file_paths = ["public_key.pem", "dify_mcp_plugin.sig", "dify_mcp_plugin.difypkg"]
    create_upload_zip(zip_name, file_paths)