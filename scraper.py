import requests
from requests.exceptions import ConnectionError
import os
import argparse
import psycopg2

DB_HOST = os.environ.get('WIKI_DB_HOST')
DB_USER = os.environ.get('WIKI_USER')
DB_DB = os.environ.get('WIKI_DB')
DB_PW = os.environ.get('WIKI_PW')

TABLE_CREATE = """
	CREATE TABLE IF NOT EXISTS articles (
		id INTEGER primary_key auto_increment,
		title VARCHAR(255),
		url VARCHAR(255),
		source VARCHAR(255),
		desc VARCHAR(1500),
		date DATE,
		search_term VARCHAR(255)
		)
		"""

#Retrives and retunrs the JSON from the BING API
def fetch(url):
 	try:
 	    req = requests.get(url,auth=HTTPBasicAuth(API_KEY,API_KEY))
 	except ConnectionError:
 	    return 'was unable to load %s' % (url)
 	if req.status_code != 200:
 	    return 'Got a %s when hitting API' % (req.status_code)
 	return req.text() 
# REtunrs a url string given a string with the search terms
def generate_url(search_term,leader,trailer):
	terms = search_term.split()
	for term in terms:
	    leader = leader + term + "+"
	print leader + trailer
	return terms
# Takes a JSON object from BING API and shoves it into a postgreSQL Db 
def load(obj):
	return None

def create_table():
	conn = psycopg2.connect('host=%s dbname=%s user=%s password=%s' % (DB_HOST,DB_DB,DB_USER,DB_PW))
	cursor = conn.cursor()
	try:
		cursor.execute(TABLE_CREATE)
		conn.commit()
	except psycopg2.ProgrammingError, e:
		conn.rollback()
	return None

if __name__ == "__main__":	
	API_KEY = os.environ.get('BING_API')
	generate_url("Barabara Boxer", "https://api.datamarket.azure.com/Bing/Search/News?$format=json&Query=%27","AND+Afforable+Care+CARE+OR+Obamacare%27")
	create_table()
