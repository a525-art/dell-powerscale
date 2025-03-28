如果是使用http   
HTTP settings>Protocol settings> Document root directory (must be within /ifs) 要去指定目錄 



#檔案內容 , 目錄列表內容 	
curl -k -u admin:P@ssw0rd   https://192.168.55.51/dir/file-name.txt

#建一個空檔	
curl -k -u admin:P@ssw0rd  -X PUT   https://192.168.55.51/upload/b1.txt

#刪檔	
curl -k -u admin:P@ssw0rd  -X DELETE https://192.168.55.51/upload/b1.txt
	
upload  local file and verify	 curl -k -u admin:P@ssw0rd -X PUT -d @b2.txt https://192.168.55.51/upload/b2.txt
curl -k -u admin:P@ssw0rd  https://192.168.55.51/upload/b2.txt
	
#建空目錄 , 上 傳檔 , 看檔 	
curl -X MKCOL  https://192.168.55.51/upload/d1 -k -u admin:P@ssw0rd
curl -k -u admin:P@ssw0rd -X PUT -d @b2.txt https://192.168.55.51/upload/d1/b2.txt
curl -k -u admin:P@ssw0rd  https://192.168.55.51/upload/d1/b2.txt

![ls -lat ]curl-ls.png
