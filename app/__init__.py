from flask import Flask

bootstrap = Bootstrap()
db = SQLAlchemy()






def create_app(config_name):
    app = Flask(__name__)
    
    #app configurations
    app.config.from_object(config_options[config_name])
    
    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    
    
    # Setting app configurations
    app.config.from_object(DevConfig)
    app.config['SECRET_KEY'] = '1234'
    app.config['WTF_CSRF_SECRET_KEY'] = '123'
    
    #registering the main app Bluprints
    from .main import main as main_bluprint
    app.register_blueprint(main_bluprint)
    
    # registering the auth blueprint
    from .auth import auth as main_bluprint
    app.register_blueprint(main_bluprint, url_prefix = '/auth')
    
    
    
    return app