#FLASK: 모노리스에서 마이크로서비스 개발방식(SW개발을 서비스 단위로 나눈 것)으로 변화하며, 나온 파이썬 프레임워크
#FLASKALCHEMY: Flask에서 SQL문을 한 가지 언어(Python)로 사용할 수 있도록 하는 확장 모듈(ORM)

#linux환경, mysql 사용 - groomide docker 컨테이너 활용


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

#개발단계이므로 에러 나오도록 진행하는 방법: debug=True
if __name__ == '__main__':
	app.run(debug=True)
