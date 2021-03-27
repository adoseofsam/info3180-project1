import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'R@nd0mK*y'
    SQLALCHEMY_DATABASE_URI = "postgresql://diuahwuowamsuy:1b30d460cd17cd9af5c0a4b5e603e675f1b57c5e89bc4e684c2f625051e90220@ec2-54-145-102-149.compute-1.amazonaws.com:5432/d60hi4p4dgs6tf"
# os.environ.get('DATABASE_URL') or 'postgresql://adoseofsam:project1pwd@localhost/webproject1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = './app/static/uploads'
    
class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
