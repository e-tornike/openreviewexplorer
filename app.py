from flask import Flask, Response, render_template
from flask_sqlalchemy import SQLAlchemy

from errors import errors
from cmap import CMAP


app = Flask(__name__)
app.register_blueprint(errors)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()


class Paper(db.Model):
    title = db.Column(db.String(256), index=True)
    tldr = db.Column(db.String(512), index=True)
    year = db.Column(db.Integer, index=True)
    score = db.Column(db.Float, index=True)
    scores = db.Column(db.String(64), index=True)
    keywords = db.Column(db.String(256), index=True)
    authors = db.Column(db.String(256), index=True)
    venue = db.Column(db.String(64), index=True)
    id = db.Column(db.String(20))
    url = db.Column(db.String(64), primary_key=True)
    decision = db.Column(db.String(32), index=True)

    def to_dict(self):
        bgcolor = CMAP.get(self.decision, "#FFFFFF")
        return {
            'title': f'<a href="{self.url}">{self.title}</a>',
            'tldr': self.tldr,
            'year': self.year,
            'keywords': self.keywords,
            'score': self.score,
            'scores': self.scores,
            'venue': self.venue,
            'authors': self.authors,
            'decision': f'<span style="background-color:{bgcolor};">{self.decision}</span>',
        } 

# db.create_all()


@app.route("/")
def index():
    return render_template('ajax_papers_table.html', title='OpenReview Explorer Plus')


@app.route('/api/data')
def data():
    papers = [paper.to_dict() for paper in Paper.query]
    return {'data': papers}


@app.route("/health")
def health():
    return Response("OK", status=200)
