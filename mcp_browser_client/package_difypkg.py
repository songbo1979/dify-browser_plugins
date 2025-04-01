import zipfile
import os

def create_difypkg(package_name, source_dir):
    difypkg_filename = f"{package_name}.difypkg"
    with zipfile.ZipFile(difypkg_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)

if __name__ == "__main__":
    package_name = "dify_mcp_plugin"
    source_dir = "dify_mcp_plugin"
    create_difypkg(package_name, source_dir)