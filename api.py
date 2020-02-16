import flask
#from api_resource.peymankaran import *
from flask_restful import Resource, Api, reqparse

app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from peymankaran import *
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
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/', methods=['download'])
def download():
    return 's'






#------------------------------------------peymankaran
@app.route('/peymankaran', methods=['POST'])
def peymankaran():
    parser = reqparse.RequestParser()
    parser.add_argument('right',required = True)
    parser.add_argument('middle',required = True)
    parser.add_argument('left',required = True)
    args = parser.parse_args()
    make_peymankaran_pdf('random_name',args)
    return str(args)

app.run()
