import os
import urllib.request
from werkzeug.datastructures import ImmutableMultiDict
from flask import Flask, request
from flask import Flask
from werkzeug.utils import secure_filename
from Modelo.Classificador import FaceCounter
import logging
from console_log import ConsoleLog

console = logging.getLogger('console')
console.setLevel(logging.DEBUG)
UPLOAD_FOLDER = 'folder'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/file-upload', methods=['POST'])
def upload_file():
    #print(request.files.to_dict(flat=True)['file'])
    if request.method == 'POST':
      file = request.files['file']
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      console.warning("[*] STARTED FUNCTION UPLOAD FILE ")
      path_frame = "folder/"+str(file.filename)
      console.warning("[*] INSTACIANDO CLASSIFICADOR")
      model = FaceCounter(path_frame)
      console.warning("[*] CONTANDO FACES...")
      total_faces = model.counter()
      console.warning("[*] CONTANDO FACES MODEL.... ")
      console.warning("[*] TOTAL DE FACES: "+str(total_faces))
      data = {"total_faces":total_faces}
      return {"mesage":"frame recebido","total_faces":str(total_faces)},200
  #except:
    #return {"mesage":"falha no parametro"},404
if __name__ == "__main__":
    app.run(debug=True)
