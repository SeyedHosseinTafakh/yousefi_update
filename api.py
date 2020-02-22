import flask

from flask_restful import Resource, Api, reqparse
import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from peymankaran import *
import glob , os
from flask import jsonify ,send_file , request


app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

#path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
#config = pdfkit.configuration()
'''options = {
    'page-size': 'A3',
     'margin-top': '0in',
     'margin-right': '0in',
     'margin-bottom': '0in',
     'margin-left': '0in',
     'orientation' : 'landscape',
}'''

@app.route('/', methods=['GET'])
def index():
    os.chdir("pdfs/")
    file_names = []
    for file in glob.glob("*.pdf"):
        file_names.append(file)
    return jsonify(file_names)
    #return "HELo world from linux"


@app.route('/download',methods=['GET'])
def download():
    file_name = request.args.get('file_name')
    path = "pdfs/"+file_name
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

#app.run(port='8080')
