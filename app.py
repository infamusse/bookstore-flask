import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
db = SQLAlchemy(app)
db.app = app

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "{title} - {author}".format(title=self.title, author=self.author)

@app.route("/")
def hello_world():
    return "<p>Hello, World from flask server!</p>"


if __name__ == "__main__":
    app.run(debug=True)