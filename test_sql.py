from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://alcology:hummussgribami@www.alcology.ru:5432/alcology')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Cocktail(Base):
    __tablename__ = 'cocktails'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    strength = Column(Integer)
    description = Column(Text)
    recipe_text = Column(Text)
    photo = Column(String(1000))
    recipe = relationship('Recipe', backref='cocktail_id')
    video = relationship('RecipeVideos', backref='cocktail_id')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Cocktail {}>'.format(self.name)


class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(Text)
    recipe = relationship('Recipe', backref='ingredient_id')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Ingredient {}>'.format(self.name)


class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    cocktail_id = Column(Integer, ForeignKey('cocktails.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    amount = Column(Integer)


class RecipeVideos(Base):
    __tablename__ = 'recipe_videos'
    id = Column(Integer, primary_key=True)
    cocktail_id = Column(Integer)
    code = Column(String(50), unique=True)

    def __init__(self, code=None):
        self.code = code

    def __repr__(self):
        return '<Video {}>'.format(self.code)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)