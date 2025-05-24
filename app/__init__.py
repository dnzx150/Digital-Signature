from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'chu-ki-so'
    from .views import main
    app.register_blueprint(main)
    return app
