from train_flask import db

class User(db.Model): #=>Base
    __tablename__ = 'user'		
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.String(32), primary_key=True) #SQLALchemy에서 굳이 여러개 갖고 올 필요가 없다.
    username=db.Column(db.String(32))