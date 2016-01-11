from flask import Flask, render_template, request
import json
from transactions import Transactions


app = Flask(__name__)

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

    return transactions.cook(retrieveRequestFor('ingredients', request).split(","))


def retrieveRequestFor(variable, request):
    if request.method == 'POST':
        return request.form[variable]
    else:
        return request.args.get(variable, '')

if __name__ == "__main__":

    #Transactions().searchByItemName("nano")
    #Transactions().cook(["2371"])
    app.run(debug=True, use_reloader=True)
