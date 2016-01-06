from flask import Flask, render_template, request, g
from bs4 import BeautifulSoup
import urllib.request
import re
import json
import sqlite3





app = Flask(__name__)
'''
app.config.update(
    SERVER_NAME="http://localhost:4500"
)
'''
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/am', methods=['POST','GET'])
def fuck():
    '''

    if request.method == 'POST':
        typeName = request.form['am']
    else:
        typeName = request.args.get('am', '')
    '''


    try:
        conn = sqlite3.connect("sqlite-latest.db")
        c = conn.cursor()

        #typeName = request.args.get('am', '')


        list = list()
        for row in c.execute("SELECT * FROM invTypes WHERE typeName LIKE '%nano%'"):
            list.append(5)
        #rv = c.fetchall()

        data = {
            "bunu gonderdin lan pic":"yalarim",
            "sik":list
        }

        return json.dumps(data)

    except :

        data = {
            "bunu gonderdin lan pic":"asdasdalarim",
            "sik":'amsin'
        }

        return json.dumps(data)
    #SELECT * FROM invTypes AS types, industryActivityMaterials as materials WHERE materials.materialTypeID = 2869 AND materials.typeID = types.typeID AND types.published = 1 ORDER BY types.typeName;













if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
