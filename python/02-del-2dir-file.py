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

# 要移除的目錄路徑
directory_to_delete = '/ifs/TC/db-1/db-2'

def delete_directory(path):
    url = f'{base_url}{path}?recursive=true'
    headers = {'x-isi-ifs-target-type': 'container'}
    response = requests.delete(url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)
    if response.status_code in [200, 202, 204]:
        print(f'目錄 {path} 及其內容已成功移除。')
    elif response.status_code == 404:
        print(f'目錄 {path} 不存在。')
    else:
        print(f'移除目錄失敗，狀態碼：{response.status_code}，訊息：{response.text}')

if __name__ == '__main__':
    delete_directory(directory_to_delete)
