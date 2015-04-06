from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from models import Movie, getMovie, addDummyData
import simplejson

app = Flask(__name__)

@app.route('/addTestData')
def addDummyStuffz():
	addDummyData()
	return 'done', 200

@app.route('/movie/all')
def getAllMovies():
	return simplejson.dumps(getMovie()) , 200

#run app
if __name__ == '__main__':
	app.run(debug=True)