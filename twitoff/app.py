from flask import Flask
from flask import render_template
from flask import request
from .models import  db, User, Tweet
import os


def create_app():

    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] =  os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    @app.route("/", methods=["GET", "POST"])
    def main():
        name = request.form.get("name")

        if name:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()

        users = User.query.all()
        return render_template("home.html", users=users, tweets=tweets)



    @app.route('/about')
    def about():
        return 'This is the coolest app ever !!!'

    @app.route('/iris')
    def iris():    
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs',
                          multi_class='multinomial').fit(X, y)

    return str(clf.predict(X[:2, :]))
    return app