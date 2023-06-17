from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

def create_database():
    with app.app_context():
        db.create_all()
        db.session.commit()

def get_db():
    """Get a database"""
    return db


def get_app():
    """Get a quart app"""
    return app