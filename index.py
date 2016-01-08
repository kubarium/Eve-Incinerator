from flask import Flask, render_template, request, g
from bs4 import BeautifulSoup
import urllib.request
import re
import json
import sqlite3
from transactions import Transactions


app = Flask(__name__)


'''
app.config.update(
    SERVER_NAME="http://localhost:4500"
)
'''
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/searchByItemName', methods=['POST','GET'])
def searchByItemName():
    transactions = Transactions()

    return transactions.searchByItemName(retrieveRequestFor('itemName', request))

@app.route('/cook', methods=['POST','GET'])
def cook():
    transactions = Transactions()
    '''

    data = {
            "package":retrieveRequestFor('ingredients', request).split(","),
            "len":5
        }
    return json.dumps(data)
    '''

    return transactions.cook(retrieveRequestFor('ingredients', request).split(","))


def retrieveRequestFor(variable, request):
    if request.method == 'POST':
        return request.form[variable]
    else:
        return request.args.get(variable, '')

if __name__ == "__main__":

    #Transactions().searchByItemName("nano")
    Transactions().cook(["2371"])
    app.run(debug=True, use_reloader=True)
