from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50) )
    gender = db.Column(db.String(10))

    weight = db.Column(db.Integer)
    hight = db.Column(db.Integer)
    heartbeat =  db.Column(db.Integer)
    phone = db.Column(db.String(20),index=True)
    cellphone = db.Column(db.String(20),index=True)
    birthday = db.Column(db.String(20))    
    address = db.Column(db.String(200))

    commit =  db.Column(db.Text)
    commit =  db.Column(db.Text)

    def __str__(self):
        return "<%s>" % self.name

    # def __repr__(self):
    #     return "%s" % self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(64) )    
    email = db.Column(db.String(120), )

    #one to one rm uselist=False is many to one
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    role = db.relationship("Role", foreign_keys=role_id, uselist=False)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username
    
    def __init__(self,username="",password="",email=""):
        self.username=username
        self.password_hash = pwd_context.encrypt(password)
        self.email=email
    
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def change_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
		
    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = Account.query.get(data['id'])
        return user

		
		
#rr=User.query.filter(Role.name=='5H8BM0',User.username=='5H8BM0').first()
#add to table
#ul=db.session.query(User.username,Role.name)
#can add join
#ul.all()

