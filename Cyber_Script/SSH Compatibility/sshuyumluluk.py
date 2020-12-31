import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.91.128',username="msfadmin",password="msfadmin")
stdin,stdout,sderr=ssh.exec_command("cat /etc/passwd")
for i in (stdout.read().decode('ascii').split("\n")):
    print(i)
