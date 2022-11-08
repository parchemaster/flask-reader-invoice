import PyPDF2
import re
import os


def find_template(textObject, f):
    if (re.search("Amazon Web Services", textObject)):
        os.rename("invoices/test.pdf", "invoices/amazon_web_services.pdf")
        # curentFile = "invoices/amazon_web_services.pdf"
    elif (re.search("Flipkart", textObject)):
        os.rename("invoices/test.pdf", "invoices/flipkart.pdf")


pdfFileObj = open('invoices/test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
textObject = pageObj.extractText()
pdfFileObj.close()
find_template(textObject, pdfFileObj)
