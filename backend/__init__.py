from flask import Flask, render_template, g, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def creat_app():
    app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/backend/static")
    # 防止跨域攻击, details:https://cloud.tencent.com/developer/article/1728658
    CORS(app)
    # 注册蓝图， details：https://dormousehole.readthedocs.io/en/latest/blueprints.html
    from . import main
    app.register_blueprint(main.main)
    app.config['SECRET_KEY'] = 'password1'
    app.debug = True
    db.init_app(app)
    return app
