from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import simplejson

app = Flask(__name__)
Engine = create_engine('sqlite:////tmp/media.sqlite3', convert_unicode=True)
Session = sessionmaker(bind=Engine)
session = Session()
Base = declarative_base()

@app.route('/movie/all')
def getAllMovies():
	movies = session.query(Movie).all()
	json = []
	for movie in movies:
		json.append({
			'id' : movie.id,
			'name' : movie.name,
			'thumbPath' : movie.thumbPath,
			'moviePath' : movie.moviePath
		})

	return simplejson.dumps(json) , 200


class Movie(Base):
	__tablename__ = 'movies'
	id = Column(Integer, primary_key = True)
	name = Column(String(80), unique=True)
	thumbPath = Column(String(150), unique=True)
	moviePath = Column(String(150), unique=True)

	def __init__(self, name,thumbPath, moviePath):
		self.name = name
		self.thumbPath = thumbPath
		self.moviePath = moviePath


Base.metadata.create_all(Engine)

#add example movie
#movie = Movie(name='hoi',thumbPath='hllk',moviePath='filmpad')
#session.add(movie)
#session.commit()

#run app
if __name__ == '__main__':
	app.run(debug=True)
