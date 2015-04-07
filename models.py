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
	json = None

	if id == None or id.upper() == 'ALL':
		movies = session.query(Movie).all()
		json = []
		for movie in movies:
			json.append(movie.toDict())
	else:
		movie = session.query(Movie).filter_by(id=id).first()
		if movie != None:
			json = movie.toDict()  
		
	return json

def getSerie(id=None):
	json = None
	if id == None or id.upper() == 'ALL':
		series = session.query(Serie).all()
		json = []
		for serie in series:
			json.append(serie.toDict())
	else:
		serie = session.query(Serie).filter_by(id=id).first()
		if serie != None:
			json = serie.toDict()
	return json

def getEpisode(id=None):
	json = None
	if id == None or id.upper() == 'ALL':
		episodes = session.query(Episode).all()
		json = []
		for episode in episodes:
			json.append(episode.toDict())
	else:
		episode = session.query(Episode).filter_by(id=id).first()
		if episode != None:
			json = episode.toDict()
	return json

def getEpisodesBySerie(serieid):
	episodes = session.query(Episode).filter_by(serie=serieid).all()
	json = []
	for episode in episodes:
		json.append(episode.toDict())
	return json

def addDummyData():
	#add example movie
	for i in range(6):
		movie = Movie(name='movie' + str(i),thumbPath='hllk' + str(i),moviePath='filmpad' + str(i))
		session.add(movie)
		serie = Serie(name='top gear' + str(i))
		session.add(serie)
		for j in range(5):
			episode = Episode(name='name', serie=i, season=j,epNumber=0)
			session.add(episode)
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

	def toDict(self):
		return {
			'id' : self.id, 'name' : self.name,
			'thumbPath' : self.thumbPath, 'moviePath' : self.moviePath
		}

class Serie(Base):
	__tablename__ = 'series'
	id = Column(Integer, primary_key=True)
	name = Column(String(80),unique=True,nullable=False)

	def __init__(self,name):
		self.name = name

	def toDict(self):
		return { 'id' : self.id, 'name' : self.name}

class Episode(Base):
	__tablename__ = 'episodes'
	id = Column(Integer, primary_key = True)
	
	#optional name
	name = Column(String(80), nullable = True)
	
	serie = Column(Integer, ForeignKey('series.id'))
	season = Column(Integer, nullable = False)
	epNumber = Column(Integer, nullable = False)

	def __init__(self,name,serie,season,epNumber):
		self.name = name
		self.serie = serie
		self.season = season
		self.epNumber = epNumber

	def toDict(self):
		return {
			'id' : self.id , 'name' : self.name,
			'serie' : self.serie, 'epNumber' : self.epNumber
		}
	
Base.metadata.create_all(Engine)