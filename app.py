import flask
from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get('WIKI_DB_HOST')
DB_USER = os.environ.get('WIKI_USER')
DB_DB = os.environ.get('WIKI_DB')
DB_PW = os.environ.get('WIKI_PW')

@app.route('/',methods=['GET','POST'])
def std():
	conn = psycopg2.connect('host=%s dbname=%s user=%s password=%s' % (DB_HOST,DB_DB,DB_USER,DB_PW))
	cur = conn.cursor()
	if request.method == 'POST':
		tags = request.form['tags']
		tags = tags.split()
		article_id = requst.form['id']
		for tag in tags:
			cur.execute("""INSERT INTO tags VALUES(%s,%s)""",(tag,article_id))
			conn.commit()
		return render_template('index.html',article=article)
	elif request.method == 'GET':
		cur.execute("SELECT * from articles order by random() limit 1")
		res = cur.fetchall()
		article = res[0]
		return render_template('index.html',article=article)
		
if __name__=="__main__":
	app.debug = True
	app.run()
