from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_migrate import Migrate
import os 
DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')  
DB_USER = os.getenv('DB_USER', 'postgres')  
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')  
DB_NAME = os.getenv('DB_NAME', 'fate')  
DB_PATH = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
db = SQLAlchemy()

def setup_db(app, database_path=DB_PATH):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)


class Servant(db.Model):
    __tablename__ = 'servant'
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    type = Column(String()) # Archer, Saber, etc..
    source = Column(String()) # Where has the servant taken from (real life figure? a book? etc)
    image = Column(String()) # insert an image of the character.
    master_id = Column(Integer, ForeignKey('master.id'))
    master = relationship('Master', back_populates='servant')
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def format(self):
        return {
            'name': self.name,
            'type': self.type,
            'source': self.source,
            'master': self.master_id
        }
    
    def __repr__(self):
        return f'Name: {self.name}, Type: {self.type}, Source: {self.source}, image: {self.image}'

class Master(db.Model):
    __tablename__ = 'master'
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    image = Column(String()) # insert an image of the character.
    servant = relationship("Servant", back_populates="master", cascade="all,delete", uselist=False) # One Master can have only one servant.

    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def format(self):
        return {
            'name': self.name,
            'image': self.image
        }
    
    def __repr__(self):
        return f'Name: {self.name}, Image: {self.image}'

if __name__ == '__main__':
    print("fine")
