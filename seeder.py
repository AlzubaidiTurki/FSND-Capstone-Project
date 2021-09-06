from models import Master, Servant
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
db = SQLAlchemy()
DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')  
DB_USER = os.getenv('DB_USER', 'postgres')  
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')  
DB_NAME = os.getenv('DB_NAME', 'fate')  
DB_PATH = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()
    emiya = Master(id=1,name='Emiya Kiritsugu', image='https://www.gwigwi.com/wp-content/uploads/2016/06/kiritsugu-emiya-e1466929284783.jpg')
    tohsaka = Master(id=2, name= 'Tohsaka Rin', image='https://2img.net/h/pre15.deviantart.net/75f5/th/pre/i/2015/079/1/0/rin_tohsaka_by_deikawn-d8fer1i.png')
    kirei = Master(id=3,name= 'Kotomine Kirei', image='https://static.myfigurecollection.net/pics/encyclopedia/4380.jpg?rev=1297513293')
    db.session.add(emiya)
    db.session.add(tohsaka)
    db.session.add(kirei)
    db.session.commit()
    archer = Servant(id=1, name='Gilgamesh', type = 'Archer', source='Epic of Gilgamesh', image='', master_id = Master.query.filter_by(name='Tohsaka Rin').first().id)
    saber = Servant(id=2, name='Artoria Pendragon', type = 'Saber',  source='Arthurian Legends', image='', master_id = Master.query.filter_by(name='Emiya Kiritsugu').first().id)
    caster = Servant(id=3, name="Gilles de Rais", type = "Caster",  source='Historical Fact', image='https://static.myfigurecollection.net/pics/encyclopedia/32393.jpg?rev=1494897149')
    db.session.add(archer)
    db.session.add(saber)
    db.session.add(caster)
    db.session.commit()
