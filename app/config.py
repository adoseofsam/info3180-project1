import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'R@nd0mK*y'
    SQLALCHEMY_DATABASE_URI = "postgresql://hjhvspmfvhpsuu:f3325165d24c6aa50453e1b52083360064b02ae82b05a8ad674f6e4c9231e769@ec2-23-21-229-200.compute-1.amazonaws.com:5432/da0kuqn3rcq48g"
# os.environ.get('DATABASE_URL') or 'postgresql://adoseofsam:project1pwd@localhost/webproject1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = './uploads'
    
class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
