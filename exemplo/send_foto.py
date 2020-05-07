from requests import post 

fin = open('jn.png', 'rb')
files = {'file': fin}
try:
   print("[*] ENVIANDO FRAME PARA API MODEL 1 - FACE COUNTE")
   r = post("http://127.0.0.1:5000/file-upload", files=files)
   print(r.json())
finally:
   fin.close()


