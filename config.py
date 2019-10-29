import os


class Config:

    '''
    Describes the general configurations
    
    '''

    SECRET__KEY = os.environ.get('12345 ')
    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:123@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # Simple MDE configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):

    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
        
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:123@localhost/blog'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
