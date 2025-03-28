import requests
from requests.auth import HTTPBasicAuth

# Isilon/PowerScale 集群信息
base_url = "https://192.168.55.51:8080"  # 请替换为您的 PowerScale 集群 IP 地址
username = "admin"  # 替换为您的用户名
password = "P@ssw0rd"  # 替换为您的密码
namespace = "ifs/TC"  # 替换为您的命名空间
directory_path = ""  # 替换为您的目录路径

# API 请求 URL
url = f"{base_url}/namespace/{namespace}/{directory_path}"

# 禁用 SSL 证书验证（仅适用于开发和测试环境）
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# 发送 GET 请求
response = requests.get(url, auth=HTTPBasicAuth(username, password), verify=False)

# 处理响应
if response.status_code == 200:
    print("Request successful.")
    print(response.json())  # 打印返回的 JSON 数据
else:
    print(f"Failed to get data. Status code: {response.status_code}")
    print(f"Error: {response.text}")
