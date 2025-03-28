import requests
import urllib3

# 忽略 SSL 憑證警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Isilon PowerScale OneFS 相關資訊
ISILON_HOST = "https://192.168.55.51"  # 伺服器地址
USERNAME = "admin"  # 使用者名稱
PASSWORD = "P@ssw0rd"  # 密碼
DELETE_PATH = "/upload/b1.txt"  # 目標刪除的文件

# API URL
url = f"{ISILON_HOST}{DELETE_PATH}"

# 發送 DELETE 請求刪除文件
response = requests.delete(url, auth=(USERNAME, PASSWORD), verify=False)

# 檢查回應結果
if response.status_code in [200, 202, 204]:
    print("文件刪除成功")
else:
    print(f"文件刪除失敗: {response.status_code} - {response.text}")
