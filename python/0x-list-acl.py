import requests
from requests.auth import HTTPBasicAuth
import urllib3
import json

# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Isilon PowerScale 叢集資訊
cluster_ip = '192.168.55.62:8080'  # 用你實際的 IP
username = 'admin'  # 用你的用戶名
password = 'P@ssw0rd'  # 用你的密碼

# 查詢指定目錄的 ACL
def get_acl(directory_path):
    url = f'https://{cluster_ip}/namespace{directory_path}?acl'  # 加入 ?acl 查詢 ACL
    response = requests.get(url, auth=HTTPBasicAuth(username, password), verify=False)

    if response.status_code == 200:
        data = response.json()  # 解析 JSON 回應內容
        print(f'目錄 {directory_path} 的 ACL 設定：')
        print(json.dumps(data, indent=4))  # 美化輸出 JSON 結果
    else:
        print(f'❌ 查詢 ACL 失敗，狀態碼：{response.status_code}，訊息：{response.text}')

# 主函數
if __name__ == '__main__':
    directory_path = '/ifs/manual'  # 設定查詢的目錄
    get_acl(directory_path)  # 呼叫函數查詢 ACL




## 這個錯誤是因為你正在嘗試在 Python 互動式環境中執行命令，這是無效的。& 是在 PowerShell 中執行命令的符號，但它不適用於 Python 互動模式。

##你應該在 PowerShell 中直接執行該命令，而不是在 Python 互動式環境中。請按以下步驟操作：

##退出 Python 互動模式：

##在 Python 互動環境中，輸入 exit() 或按 Ctrl+Z 並按 Enter 來退出 Python 互動模式。

##在 PowerShell 中執行 Python 腳本：

##打開 PowerShell，然後執行以下命令：

#python3.13.exe c:/Users/angelo/py/62-4-list-ACL.py
##這樣，你的 Python 腳本就會正常運行，並且你應該會看到結果。如果還有任何錯誤或問題，請隨時告訴我。
