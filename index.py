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
        conn = sqlite3.connect("sqlite-latest.sqlite")
        conn.text_factory =  lambda x: str(x, 'latin1')
        c = conn.cursor()

        #typeName = request.args.get('am', '')


        list = []

        for row in c.execute("SELECT * FROM invTypes WHERE typeName LIKE ?", ("%nano%",)):
            list.append(row)
        #rv = c.fetchall()

        data = {
            "am":"sikmek istiyorum",
            "sik":list
        }

        return json.dumps(data)

    except sqlite3.Error as er:

        data = {
            "yardirsan":"artik",
            "sik":er
        }

        return json.dumps(data)
    #SELECT * FROM invTypes AS types, industryActivityMaterials as materials WHERE materials.materialTypeID = 2869 AND materials.typeID = types.typeID AND types.published = 1 ORDER BY types.typeName;



if __name__ == "__main__":
    #fuck()
    app.run(debug=True, use_reloader=True)
