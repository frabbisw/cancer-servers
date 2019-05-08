import os
from flask import Flask, request, redirect, url_for
from api.doctor import Doctor
import json
from flask import jsonify

app = Flask(__name__)

@app.route('/doctors', methods=['POST'])
def getDoctor():
    lat = request.form['lat']
    lon = request.form['lon']
        
    
    doc1 = Doctor("23.2", "89.4", "Mr. Abul", "Poropar Hospital")
    doc2 = Doctor("24.3", "90.4", "Mr. Babul", "Vobolila Hospital")
    doc3 = Doctor("22.9", "90.1", "Mr. Cabul", "Moron Hospital")
    doc4 = Doctor("21.9", "90.1", "Mr. Dablu", "FarCry Hospital")

    docs = []

    docs.append(doc1)
    docs.append(doc2)
    docs.append(doc3)

    #js = jsonify(docs)

    print(doc1.toJSON())

    return "["+doc1.toJSON()+","+doc2.toJSON()+","+doc3.toJSON()+","+doc4.toJSON()+"]"