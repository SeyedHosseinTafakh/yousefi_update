from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


title = 'title test'
def drawMyRuler(pdf):
    pdf.drawString(100,810,'x100')
    pdf.drawString(200,810,'x200')
    pdf.drawString(300,810,'x300')
    pdf.drawString(400,810,'x400')
    pdf.drawString(500,810,'x500')

    pdf.drawString(10,100,'x100')
    pdf.drawString(10,200,'x200')
    pdf.drawString(10,300,'x300')
    pdf.drawString(10,400,'x400')
    pdf.drawString(10,500,'x500')
    pdf.drawString(10,600,'x600')
    pdf.drawString(10,700,'x700')
    pdf.drawString(10,800,'x800')


pdf = canvas.Canvas('C:/Users/hossein/Desktop/pdf maker/sample.pdf')
drawMyRuler(pdf)


pdf.setFont('Courier',size=50)
pdf.setTitle(title)

pdf.drawString(270,770,title)

pdf.save()




print('Done')
