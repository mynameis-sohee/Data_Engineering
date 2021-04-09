'''프린트 분리이유: 파일 구조화 / 오류 수정 용이성이 주 원인이다. 또한 route가 동일할 경우 충돌의 문제가 발생할 수 있으므로, 블루프린트 분리를 함으로써 서로 간 의존성을 수 있기에 사용한다.
보통 views 폴더 내 'name_views.py'의 형태로 저장된다.'''


######### main_views.py ###########
from flask import Blueprint
from train_flask import db
from train_flask.models.user_model import User


#블루프린트의 이름(추후 url_for 등에서 활용됨), import할 때의 모듈이름, URL 프리픽스(url_prefix)값 전달
main_bp = Blueprint('main',__name__,url_prefix='/main')

@main_bp.route('/')
def main_name():
    new_user=User(username='patrick')
    db.session.add(new_user)
    return 'patrick', 201

@main_bp.route('/index')
def main_index():
    return 'index', 200



######### __init__.py ###########
from flask import Flask

def create_app():
    app = Flask(__name__)
 
    from .views import main_views
    app.register_blueprint(main_views.bp)  

    return app
