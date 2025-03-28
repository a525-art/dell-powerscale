import os
import requests
from requests.auth import HTTPBasicAuth
import urllib3

# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# PowerScale 叢集資訊
cluster_ip = '192.168.55.51:8080'
username = 'admin'
password = 'P@ssw0rd'

# 基本 URL
base_url = f'https://{cluster_ip}/namespace'

# 要創建的目錄和子目錄路徑
directory_path = '/ifs/TC/db-1/db-2'

# 本地檔案路徑
local_file_path = 'sample.txt'

# 遠端檔案路徑
remote_file_path = f'{directory_path}/sample.txt'

# 創建目錄（包括父目錄）
def create_directory(path):
    url = f'{base_url}{path}?recursive=true'
    headers = {'x-isi-ifs-target-type': 'container'}
    response = requests.put(url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)
    if response.status_code in [201, 204]:
        print(f'目錄 {path} 創建成功。')
    elif response.status_code == 200:
        print(f'目錄 {path} 已存在。')
    else:
        print(f'創建目錄失敗，狀態碼：{response.status_code}，訊息：{response.text}')

# 上傳檔案
def upload_file(remote_path, local_path, overwrite=True):
    url = f'{base_url}{remote_path}?overwrite={str(overwrite).lower()}'
    headers = {'x-isi-ifs-target-type': 'object'}
    with open(local_path, 'rb') as file_data:
        response = requests.put(url, headers=headers, data=file_data, auth=HTTPBasicAuth(username, password), verify=False)
    if response.status_code in [201, 200]:
        print(f'檔案 {remote_path} 上傳成功。')
    else:
        print(f'上傳檔案失敗，狀態碼：{response.status_code}，訊息：{response.text}')

if __name__ == '__main__':
    # 檢查本地檔案是否存在
    if not os.path.isfile(local_file_path):
        print(f'本地檔案 {local_file_path} 不存在。請確認檔案路徑正確。')
    else:
        create_directory(directory_path)
        upload_file(remote_file_path, local_file_path, overwrite=True)
