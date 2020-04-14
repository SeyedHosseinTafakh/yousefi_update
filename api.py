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
from natayej_koli import *
from a_56_inch import *
from a_30_inch import *
from jadval_peymankaran import *
from jadval_arazi import *

from model_mali import *
from gostare_ha import *
from natayej_koli_dollar import *
from jadval_56_dollar import *
from jadval_36_dollar import *

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
#    return "s"
    data = pd.read_csv('data.csv').T
    indexes = ['tarikh','shomare_ghest','onvan','esme_file']
    data.index = indexes
    data = data.to_json()
    return data


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
            return 'error : id_ghest required'
        make_pishraft_fiziki_pdf(args['id_ghest'])
    if args['type'] =='tahsil_arazi':
        make_arazi_pdf()
    if args['type'] =='compressors':
        make_torbocompresssor_pdf()
    if args['type'] =='pardakht_naftanir':
        make_pardakht_shode_tavasote_naftanir()
    
    if args['type'] =='peymankaran':
        make_peymankaran_pdf()
    if args['type']=='jadval_56':
        make_jadval_56()
    if args['type'] =='jadval_30':
        make_jadval_36()
    if args['type'] == 'jadval_sadid_mahshahr':
        make_jadval_sadid_mahshahr()
    if args['type'] == 'taahodat_mohandesi':
        if not 'id_ghest' in args:
             return 'error : id_gosrare required'
        make_tahodat_mohandesi_pdf(args['id_ghest'])
    if args['type'] == 'taahodate_naftanir':
        if not 'id_ghest' in args:
            return 'error : id_gosrare required'
        make_tahodat_naftanir_pdf(args['id_ghest'])
    if args['type']=='natayej_koli':
        make_natayej_koli()
    if args['type']=='56_inch':
        make_56_pdf()
    if args['type']=='30_inch':
        make_30_pdf()
    if args['type']=='jadval_peymankaran':
        make_jadval_peymankaran()
    if args['type']=='jaraem_takhir_dar_bahre_bardari':
        if not 'id_ghest' in args:
            return 'error : id_gosrare required'
        make_jaraem_takhir_dar_bahre_bardari(args['id_ghest'])
    if args['type']=='jadval_arazi':
        jadval_arazi_pdf()
    if args['type']=='model_mali':
        jadval_arazi_pdf()
    if args['type']=='gostare_ha':
        if not 'id_ghest' in args:
            return 'error : id_gosrare required'
        if not 'id_gostare' in args:
            return 'error : id_gosrare required'
        make_gostare_pdf(args['id_ghest'] , args['id_gostare'])
    if args['type']=='natayej_koli_dollar':
        make_natayej_koli_d()
    if args['type']=='jadval_56_dollar':
        make_jadval_56_dollar()
    if args['type']=='jadval_36_dollar':
        make_jadval_36_dollar()
    return "OK"



app.run(port=50000)
