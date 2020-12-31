import requests
dosya=open("fuzzing.txt","r")
icerik=dosya.read()
dosya.close()

#Burada ki cookie bilgisi değişiklik gösteriri siz kendi cookie bilginizi koyacaksınız.
header={"Cookie": "security=high; PHPSESSID=0639ced4e3b12926d1508f2dcf117b00"}

for i in icerik.split("\n"):
    print(i)
    url="http://192.168.91.128"+str(i)
    sonuc=requests.get(url=url, headers=header)
    if "200" in str(sonuc.status_code):
        print("Dosya veya dizin var:",i)
    else:
        print("Dosya veya dizin yok:",i)
