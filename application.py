from flask import Flask, render_template
"""
application.py, main.py - sao pontos de entrada do programa. 
"""
application = Flask(__name__)
@application.route('/')

def main():
    return render_template('index.html')