import flask
#from api_resource.peymankaran import *
from flask_restful import Resource, Api, reqparse
import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from peymankaran import *
import glob , os
from flask import jsonify ,send_file


app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
options = {
    'page-size': 'A3',
     'margin-top': '0in',
     'margin-right': '0in',
     'margin-bottom': '0in',
     'margin-left': '0in',
     'orientation' : 'landscape',
}

@app.route('/', methods=['GET'])
def home():
    os.chdir("pdfs/")
    file_names = []
    for file in glob.glob("*.pdf"):
        file_names.append(file)
    return jsonify(file_names)



@app.route('/download',methods=['POST'])
def download():
    parser = reqparse.RequestParser()
    parser.add_argument('file_name', required=True)
    args = parser.parse_args()
    path = "pdfs/"+args['file_name']
    return send_file(path, as_attachment=True)


#------------------------------------------peymankaran
@app.route('/peymankaran', methods=['POST'])
def peymankaran():
    parser = reqparse.RequestParser()
    parser.add_argument('right',required = True)
    parser.add_argument('middle',required = True)
    parser.add_argument('left',required = True)
    parser.add_argument('name',required = True)
    args = parser.parse_args()
    make_peymankaran_pdf(args['name'],args)
    return str(args)

app.run()
