import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="AndrewLambert",
    password="Be0wawe1",
    hostname="AndrewLambert.mysql.pythonanywhere-services.com",
    databasename="AndrewLambert$wolvapp",
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False