import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#İp adresi, username ve password sizde farklılık gösterebilir.
ssh.connect('192.168.91.128',username="msfadmin",password="msfadmin")
stdin,stdout,stderr=ssh.exec_command("ls")
print(stdout.read())