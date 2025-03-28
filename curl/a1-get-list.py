## 注意哦 curl 下的python 是用 http request 的方式去作業的 不是叫RAST API
import requests
import urllib3

# 忽略 SSL 憑證警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Isilon OneFS REST API 配置
ISILON_HOST = "https://192.168.55.51"
USERNAME = "admin"
PASSWORD = "P@ssw0rd"

# REST API 根端點
url = f"{ISILON_HOST}/upload"

# 發送 GET 請求
response = requests.get(url, auth=(USERNAME, PASSWORD), verify=False)

# 檢查請求結果
if response.status_code == 200:
    print("請求成功，回應內容：")
    print(response.text)
else:
    print(f"請求失敗，錯誤碼: {response.status_code}")
    print("錯誤訊息:", response.text)

