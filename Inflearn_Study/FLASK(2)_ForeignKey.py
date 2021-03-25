# one-to-many 관계, User의 role_id는 Role의 id이다.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/dbname'

db = SQLAlchemy(app)
    
    
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(50))
    users = db.relationship('User',backref='role',lazy='dynamic') #위 외래키연결을 위해 작성. backref: 테이블명(전체 소문자), lazy: 받는 방식 
    
    def __repr__(self):
        return '<Role %r>' % self.position
    
    

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id')) #Role의 id를 외래키로 가져오겠다는 의미(테이블은 전부 소문자로 인식)
    
    def __repr__(self):
        return "{self.id}, {self.username}"
    

