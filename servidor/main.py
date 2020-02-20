# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash
from contact_model import Contac

app = Flask(__name__)
app.secret_key = 'some_secret'
app.debug = True

@app.route(r'/', methods=['GET'])
def contact_book():
    contacts = Contac.query().fetch()
    return render_template('contact_book.html', contacts=contacts)

@app.route(r'/add', methods=['GET','POST'])
def add_contact():
    if request.form:
        contac = Contac(name=request.form.get('name'),
                        phone=request.form.get('phone'),
                        email=request.form.get('email'))
        contac.put()
        flash('Contacto Añadido')
    
    return render_template('add_contact.html')

@app.route(r'/contacto/<uid>', methods=['GET'])
def contac_details(uid):
    contacto = Contac.get_by_id(int(uid))
    return render_template('contact.html', contact=contacto)
 
if __name__ == "__main__":
    app.run()