import requests


response=requests.get("https://www.usom.gov.tr/url-list.txt",verify=False)

dosya=open("usom.txt","w")
dosya.write(str(response.content))
dosya.close


"""def kontrol_et(ip):
    dosya=open("usom.txt","r")
    icerik=dosya.read()
    dosya.close()
    if str(ip) in icerik:
        print("IP zararlıdır.")
    else:
        print("IP zararlı değil.")

ip=str(input("Lütfen bir IP Giriniz: "))
kontrol_et(ip)"""
    


