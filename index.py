from flask import Flask, render_template
from bs4 import BeautifulSoup
import urllib.request
import re
import json
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/am')
def fuck():
    data = {"siksinler":"seni"}
    return json.dumps(data)
    #SELECT * FROM invTypes AS types, industryActivityMaterials as materials WHERE materials.materialTypeID = 2869 AND materials.typeID = types.typeID AND types.published = 1 ORDER BY types.typeName;


if __name__ == "__main__":
    app.run(use_reloader=True)