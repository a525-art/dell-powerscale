import requests
import urllib3

# 忽略 SSL 憑證警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Isilon PowerScale OneFS 相關資訊
ISILON_HOST = "https://192.168.55.51"  # 伺服器地址
USERNAME = "admin"  # 使用者名稱
PASSWORD = "P@ssw0rd"  # 密碼
DIRECTORY_PATH = "/upload/d1"  # 要創建的目錄路徑

# API URL
url = f"{ISILON_HOST}{DIRECTORY_PATH}"

# 發送 MKCOL 請求以創建目錄
response = requests.request("MKCOL", url, auth=(USERNAME, PASSWORD), verify=False)

# 檢查回應結果
if response.status_code in [201, 200]:
    print("目錄創建成功")
else:
    print(f"目錄創建失敗: {response.status_code} - {response.text}")
