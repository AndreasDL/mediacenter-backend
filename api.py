from flask import Flask, Response
from flask.ext.sqlalchemy import SQLAlchemy
from models import getMovie, getSerie, getEpisode, getEpisodesBySerie
from models import addDummyData
import simplejson

app = Flask(__name__)

@app.route('/addTestData')
def addDummyStuffz():
	addDummyData()
	return 'done', 200

@app.route('/movie/<movieid>')
def getMovieByID(movieid):
	movies = getMovie(movieid)
	if movies == None:
		return 'no movies found', 404
	else:
		return Response(simplejson.dumps(movies), content_type='application/json') , 200

@app.route('/serie/<serieid>')
def getSerieByID(serieid):
	series = getSerie(serieid)
	if series == None:
		return 'no series found', 404
	else:
		return Response(simplejson.dumps(series), content_type='application/json'), 200

@app.route('/episode/<episodeid>')
def getEpisodeByID(episodeid):
	episodes = getEpisode(episodeid)
	if episodes == None:
		return "no episodes found", 404
	else:
		return Response(simplejson.dumps(episodes), content_type='application/json'), 200

@app.route('/episode/bySerieID/<serieid>')
def getEpisodesBySerieID(serieid):
	episodes = getEpisodesBySerie(serieid)
	return Response(simplejson.dumps(episodes), content_type='application/json'), 200

#run app
if __name__ == '__main__':
	app.run(debug=True)