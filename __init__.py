from flask import Flask

def create_app():

	app = Flask(__name__) #현재 폴더의 이름을 갖고 옵니다. 그 이름이 main이면 아래 if문이 활성화되겠죠.
	@app.route('/')
	def random_func():
		# breakpoint(),print(): 본인이 실행한 터미널 창에서 실행할 수 있다.
		return 'write', 200

	from view.main_view import main_bp # 만든 블루프린트를 해당 페이지로 import
	app.register_blueprint(main_bp) #만든 블루프린트가 해당 페이지에서 활성화될 수 있도록 연결

	return app

if __name__ == '__main__':
	app = create_app()
	app.run(debug=True) #개발단계이므로 에러 나오도록 진행