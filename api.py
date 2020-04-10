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


#--------------------------------------------
from pishraft_fiziki import *
from tahsil_arazi import *
from compressor import * 
from pardakht_shode_tavasote_naftanir import *
from jadval56 import *
from jadval36 import *
from jadval_sadid_mahshahr import *
from taahodat_mohandesi import *
from taahodate_naftanir import *
from jaraem_takhir_dar_bahre_bardari import *





app = flask.Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

'''
app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True
cors = CORS(api, resources={r"": {"origins": "*"}})
'''
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


# @app.route('/download',methods=['GET'])
# def download():
#     file_name = request.args.get('file_name')
#     path = "pdfs/"+file_name
#     return send_file(path, as_attachment=True)


#------------------------------------------peymankaran
@app.route('/SendData', methods=['POST'])
def peymankaran():
    if not request.is_json:
        return 'error just json format'
    args = request.get_json()
    if args['type'] == 'pishraft_fiziki':
        if not 'id_ghest' in args:
            return 'error : id_gosrare required'
        make_pishraft_fiziki_pdf(args['id_ghest'])
    if args['type'] =='tahsil_arazi':
        make_arazi_pdf()
    if args['type'] =='compressors':
        make_torbocompresssor_pdf()
    if args['type'] =='pardakht_naftanir':
        make_pardakht_shode_tavasote_naftanir()
    if args['type'] == 'tahsil_arazi':
        make_arazi_pdf()
    if args['type'] =='peymankaran':
        make_peymankaran_pdf()
    #todo :: add peymankaran_jadval
    if args['type']=='jadval_56':
        make_jadval_56()
    if args['type'] =='jadval_30':
        make_jadval_36()
    if args['type'] == 'jadval_sadid_mahshahr':
        make_jadval_sadid_mahshahr()
    if args['type'] == 'taahodat_mohandesi':
        make_tahodat_mohandesi_pdf()
    if args['type'] == 'taahodate_naftanir':
        make_tahodat_naftanir_pdf()
    if args['type'] =='jaraem_takhir_dar_bahre_bardari':
        make_jaraem_takhir_dar_bahre_bardari(id_gostare=args['id_gostare'] , id_ghest = args['id_ghest'])
    return "OK"


app.run(port=50000)
