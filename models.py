from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Engine = create_engine('sqlite:///./media.sqlite3', 
	convert_unicode=True, 
#	echo=True
)
Session = sessionmaker(bind=Engine)
session = Session()
Base = declarative_base()

def getMovie(id=None):
	movies = []
	if id == None:
		movies = session.query(Movie).all()
	else:
		movies = session.query(Movie).filter_by(id=id).first()
		
	json = []
	for movie in movies:
		json.append({
			'id' : movie.id,
			'name' : movie.name,
			'thumbPath' : movie.thumbPath,
			'moviePath' : movie.moviePath
		})
	return json

def addDummyData():
	#add example movie
	movie = Movie(name='hoi',thumbPath='hllk',moviePath='filmpad')
	session.add(movie)
	session.commit()

# ------------------------------------
# classes
# ------------------------------------
class Movie(Base):
	__tablename__ = 'movies'
	id = Column(Integer, primary_key = True)
	name = Column(String(80), unique=True,nullable=False)
	thumbPath = Column(String(150), unique=True,nullable=False)
	moviePath = Column(String(150), unique=True,nullable=False)

	def __init__(self, name,thumbPath, moviePath):
		self.name = name
		self.thumbPath = thumbPath
		self.moviePath = moviePath

class Serie(Base):
	__tablename__ = 'series'
	id = Column(Integer, primary_key=True)
	name = Column(String(80),unique=True,nullable=False)

class Episode(Base):
	__tablename__ = 'episodes'
	id = Column(Integer, primary_key = True)
	
	#optional name
	name = Column(String(80), nullable = True)
	
	serie = Column(Integer, ForeignKey('series.id'))
	season = Column(Integer, nullable = False)
	number = Column(Integer, nullable = False)
	
Base.metadata.create_all(Engine)