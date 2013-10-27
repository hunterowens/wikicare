import requests
import pymongo
import os
import argparse

API_KEY = os.environ.get('BING_API')

#Retrives and retunrs the JSON from the BING API
def fetch(url):
	try:
		req = requests.get(url,auth=HTTPBasicAuth(API_KEY,API_KEY)
	except ConnectionError:
		return 'was unable to load %s' % (url)
	if req.status_code != 200:
		return 'Got a %s when hitting API' % (req.status_code)
	return req.text() 
# REtunrs a url string given a string with the search terms
def generate_url(s):
	
# Takes a JSON object from BING API and shoves it into a MongoDB collection
def load()

if __name__ == "__main__"	
