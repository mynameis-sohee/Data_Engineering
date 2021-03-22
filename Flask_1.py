from flask import Flask

app = Flask(__name__)

@app.route('/')
def random_func():
	# breakpoint(),print(): 본인이 실행한 터미널 창에서 실행할 수 있다.
	return 'write', 200

if __name__ == '__main__':
	app.run(debug=True) #개발단계이므로 에러 나오도록 진행
