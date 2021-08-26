import re
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a, b))

@app.route('/sub')
def sub_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a, b))

@app.route('/mult')
def mult_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a, b))

@app.route('/div')
def div_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a, b))


# all-in-one route

operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<op>')
def do_math(op):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = operators[op](a, b)
    return str(result)