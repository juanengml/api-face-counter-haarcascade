from requests import post

#endpoint = "https://IckyBronzeAbstracttype.juanengml.repl.co/file-upload"

endpoint = "https://IllLiveRepo.juanengml.repl.co/Upload_img/Contador_faces/"
while True:
 fin = open('mulheres.png', 'rb')
 files = {'file': fin}
 try:
    print("[*] ENVIANDO FRAME PARA API MODEL 1 - FACE COUNTE")
    r = post(endpoint, files=files)
    print(r.json())
 finally:
    fin.close()
 fin = open('jn.png', 'rb')
 files = {'file': fin}
 try:
    print("[*] ENVIANDO FRAME PARA API MODEL 1 - FACE COUNTE")
    r = post(endpoint, files=files)
    print(r.json())
 finally:
    fin.close()
