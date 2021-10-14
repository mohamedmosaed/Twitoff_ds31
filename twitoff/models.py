from flask_sqlalchemy import SQLAlchemy

# Creates a 'user' table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # id as primary key
    name = db.Column(db.String(50), nullable=False) # user name

    def __repr__(self):
        return "<User: {}>".format(self.name)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True) # id as primary key
    test = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", backref=db.backref('tweets', lazy=True))
    word2vec = db.Column(db.PickleType,  nullable=False)

    def __repr__(self):
        return "Tweet: {}>".format(self.text)
