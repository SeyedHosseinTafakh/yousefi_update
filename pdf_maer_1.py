import pdfkit 
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
#options={'page-size':'A4', 'dpi':400,'disable-smart-shrinking': ''}
options = {
    'page-size': 'A3',
     'margin-top': '0in',
     'margin-right': '0in',
     'margin-bottom': '0in',
     'margin-left': '0in',
     'orientation' : 'landscape',
}



pdfkit.from_file('shandool2.html', 'out.pdf',configuration=config , options=options)


