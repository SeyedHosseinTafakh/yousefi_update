import flask
import platform
from flask_restful import Resource, Api, reqparse
import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from peymankaran import *
import glob , os
from flask import jsonify ,send_file , request
import pathlib
from flask_cors import CORS
from pishraft_fiziki import *
app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"": {"origins": ""}})

#path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
#config = pdfkit.configuration()

@app.route('/', methods=['GET'])
def index():
    path = path = pathlib.Path().absolute().__str__()
    #os.chdir(path+"/pdfs/")
    file_names = []
    for file in glob.glob("pdfs/*.pdf"):
                
        if platform.system() =='Linux':
            
            file=file.replace('pdfs/','')
        else:
            file = file.replace('pdfs\\','')
        file_names.append(file)
    return jsonify(file_names)
    #return "HELo world from linux"


@app.route('/download',methods=['GET'])
def download():
    file_name = request.args.get('file_name')
    path = "pdfs/"+file_name
    return send_file(path, as_attachment=True)


#------------------------------------------peymankaran
@app.route('/SendData', methods=['POST'])
def peymankaran():
    if not request.is_json:
        return 'error just json format'
    args = request.get_json()
    if args['type'] == 'pishraft_fiziki':
        if not 'id_gostare' in args:
            return 'error : id_gosrare required'
        make_pishraft_fiziki_pdf(args['id_gostare'])
    return "OK"


#app.run(port=8080)
