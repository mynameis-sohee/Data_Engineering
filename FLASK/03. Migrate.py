#pip install Flask-Migrate

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

#app을 return할 create_app 함수 생성
def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mini_flask.sqlite3'
    
    db.init_app(app)
    migrate.init_app(app, db)

    return app
    
if __name__ == "__main__":
    app.run(debug=True)
