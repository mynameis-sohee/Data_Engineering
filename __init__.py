from flask import Flask
from flask_sqlalchemy import SQLAlchemy #편리하게 SQLAlchemy를 생성할 수 있다.
from flask_migrate import Migrate

db = SQLAlchemy() #하나의 인스턴스를 생성
migrate = Migrate() #해당 db의 변동사항 등을 관리(생성(init),변경사항 업데이트(migrate) 반영(upgrade) falsk db {})

def create_app():

	app = Flask(__name__) #현재 폴더의 이름을 갖고 옵니다. 그 이름이 main이면 아래 if문이 활성화되겠죠.
	app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flask_db.sqlite3'#어떤 SQL을 사용할지 엔진을 인지
	db.init_app(app) # db하나의 인스턴스를 생성
	migrate.init_app(app, db) #해당 db의 변동사항 등을 관리(생성(init),변경사항 업데이트(migrate) 반영(upgrade) falsk db {})


	class User(db.Model): #=>Base
		__tablename__ = 'user'
		
		id=db.Column(db.String(32), primary_key=True) #SQLALchemy에서 굳이 여러개 갖고 올 필요가 없다.
		username=db.Column(db.String(32))

	#db.drop_all() #db 지우는 것
	#db.create_all() #db 생성된 것

	
	@app.route('/')
	def random_func():
		# breakpoint(),print(): 본인이 실행한 터미널 창에서 실행할 수 있다.
		
		return 'write', 200

	from train_flask.views.main_view import main_bp # 만든 블루프린트를 해당 페이지로 import
	app.register_blueprint(main_bp) #만든 블루프린트가 해당 페이지에서 활성화될 수 있도록 연결

	return app

if __name__ == '__main__':
	app = create_app()
	app.run(debug=True) #개발단계이므로 에러 나오도록 진행