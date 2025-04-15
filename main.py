from flask import Flask, render_template
from data.users import User
from data.jobs import Jobs

from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    for i in jobs:
        t_l = db_sess.query(User).filter(User.id == i.team_leader).first()
        i.team_leader = f'{t_l.surname} {t_l.name}'
    return render_template("index.html", jobs=jobs)


if __name__ == '__main__':
    main()
