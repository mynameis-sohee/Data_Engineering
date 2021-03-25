from flask_sqlalchemy import SQLAlchemy
from flask import Flask 

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://private'
db=SQLAlchemy(app)

#Role, Member, Project 생성

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(50))
    
    #one-many관계
    members = db.relationship('Member', backref='role', lazy='dynamic')

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

#one-many관계
    role_id=db.Column(db.Integer, db.ForeignKey('role.id'))

#many-many관계 - member_project
    projects=db.relationship('Project',secondary='member_project', backref='member', lazy='dynamic')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
#many-many관계 - member_project
    members=db.relationship('Member',secondary='member_project', backref='project', lazy='dynamic')


#many-many관계
#db.Table('해당 테이블명', db.Column('해당컬럼에서의 컬럼명', db.형식, db.ForeignKey('가져올 테이블명(default:소문자).가져올 컬럼명'), db.Column(이하 동일))
db.Table('member_project',
    db.Column('member_id', db.Integer,db.ForeignKey('member.id')),
    db.Column('project_id', db.Integer,db.ForeignKey('project.id'))
    )
