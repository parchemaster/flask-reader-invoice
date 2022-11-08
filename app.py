from email.policy import default
from datetime import datetime
from flask import Flask, redirect, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import PyPDF2
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
import re
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoices.db'
db = SQLAlchemy(app)


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(100), nullable=False)
    sender = db.Column(db.String(100), nullable=False)
    receiver = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(), default=False)
    orders = db.Column(db.Integer(), nullable=False)
    amount = db.Column(db.Float(), nullable=True)


file_name = ""


def find_template(textObject):
    global file_name
    if (re.search("Amazon Web Services", textObject)):
        os.rename("invoices/test.pdf", "invoices/amazon_web_services.pdf")
        file_name = "amazon_web_services.pdf"
    elif (re.search("Flipkart", textObject)):
        os.rename("invoices/test.pdf", "invoices/flipkart.pdf")
        file_name = "flipkart.pdf"
    elif (re.search("QualityHosting", textObject)):
        os.rename("invoices/test.pdf", "invoices/quality_hosting.pdf")
        file_name = "quality_hosting.pdf"
    elif (re.search("Sammy Maystone", textObject)):
        os.rename("invoices/test.pdf", "invoices/sammy_maystone.pdf")
        file_name = "sammy_maystone.pdf"
    elif (re.search("Free", textObject)):
        os.rename("invoices/test.pdf", "invoices/free_fiber.pdf")
        file_name = "free_fiber.pdf"


# @app.route('/convertPDF', methods=['POST'])
# def convert():
#     if request.method == 'POST':
        # f = request.files['file']
        # f.save("invoices/test.pdf")
        # pdfFileObj = open('invoices/test.pdf', 'rb')
        # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # print(pdfReader.numPages)
        # pageObj = pdfReader.getPage(0)
        # textObject = pageObj.extractText()
        # pdfFileObj.close()

        # find_template(textObject)

        # templates = read_templates('templates/')
        # invoice = extract_data("invoices/" + file_name, templates=templates)
        # print(invoice)

#         # number = invoice.invoice_number
#         # sender = invoice.partner_name
#         # receiver = "Sharai Ivan"
#         # date = invoice.date
#         # orders = invoice.lines.len()
#         # amount = 200

#         # invoice = Invoice(number=number, sender=sender,
#         #                   receiver=receiver, date=date, orders=orders, amount=amount)

        # try:
        #     db.session.add(invoice)
        #     db.session.commit()
        #     return redirect("asd")
        # except:
        #     return "Error with adding new element to DB"

#         return invoice

@app.route('/convertPDF', methods=['POST'])
def convert():
    if request.method == 'POST':
        f = request.files['file']
        f.save("invoices/test.pdf")
        pdfFileObj = open('invoices/test.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        print(pdfReader.numPages)
        pageObj = pdfReader.getPage(0)
        textObject = pageObj.extractText()
        pdfFileObj.close()

        find_template(textObject)

        templates = read_templates('templates/')
        invoice = extract_data("invoices/" + file_name, templates=templates)
        print(invoice)

        return invoice


if __name__ == '__main__':
    app.run(debug=True)


# templates = read_templates('templates/')
# invoice = extract_data('invoices/test4.pdf', templates=templates)
# print(invoice)

# can not call atribute

# number = invoice['invoice_number']
# sender = invoice['partner_name']
# receiver = "Sharai Ivan"
# date = invoice['date']
# orders = invoice['lines']
# amount = invoice['amount']
