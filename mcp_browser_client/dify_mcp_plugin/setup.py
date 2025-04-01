from setuptools import setup, find_packages

setup(
    name='dify_mcp_plugin',
    version='0.1.0',
    description='A Dify Agent plugin for MCP server connection',
    author='songbo',
    author_email='songbo-email@126.com',
    packages=find_packages(),
    install_requires=[
        'requests',  # 如果你使用了 requests 库
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)