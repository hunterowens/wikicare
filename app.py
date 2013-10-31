import flask
from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get('WIKI_DB_HOST')
DB_USER = os.environ.get('WIKI_USER')
DB_DB = os.environ.get('WIKI_DB')
DB_PW = os.environ.get('WIKI_PW')

@app.route('/')
def std():
	conn = psycopg2.connect('host=%s dbname=%s user=%s password=%s' % (DB_HOST,DB_DB,DB_USER,DB_PW))
	cursor = conn.cursor()
	return render_template('index.html')

if __name__=="__main__":
	app.debug = True
	app.run()
