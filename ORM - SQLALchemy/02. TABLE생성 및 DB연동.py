from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


@app.route('/')
def random_func():
	# breakpoint(),print(): 본인이 실행한 터미널 창에서 실행할 수 있다.
	return 'write', 200


#SQLAlchemy 이용한 DB연동기능 추가, User 테이블 생성
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/database_name'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False) #빈값 허용여부:nullable

#sql검색 시, 해당 repr 설정값에 맞게 출력
def __repr__(self):
    return '<User>' % self.id % self.username
