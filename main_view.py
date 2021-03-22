#블루프린트 분리이유: route가 동일하거나의 경우에, 충돌이 일어날 수 있다. 따라서 분리가 중요하다. 서로 간 의존성을 없애기 위함이다.

from flask import Blueprint

main_bp = Blueprint('main',__name__) #블루프린트의 이름, import할 때 이름

@main_bp.route('/')
def main_index():
	return 'patrick',202
