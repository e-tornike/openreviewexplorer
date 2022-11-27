from flask import Flask, Response, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

from errors import errors

app = Flask(__name__)
app.register_blueprint(errors)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()


class Paper(db.Model):
    title = db.Column(db.String(128), index=True)
    year = db.Column(db.Integer, index=True)
    score = db.Column(db.Float, index=True)
    scores = db.Column(db.String(64), index=True)
    decision = db.Column(db.String(20), index=True)
    # keywords = db.Column(db.String, index=True)
    # authors = db.Column(db.String(128), index=True)
    venue = db.Column(db.String(64), index=True)
    id = db.Column(db.String(20))
    url = db.Column(db.String(64), primary_key=True)

    def to_dict(self):
        return {
            'title': f'<a href="{self.url}">{self.title}</a>',
            'year': self.year,
            'score': self.score,
            'scores': self.scores,
            'decision': self.decision,
            'venue': self.venue,
            'id': self.id,
            'url': f'<a href="{self.url}">Source</a>'
        }

db.create_all()


@app.route("/")
def index():
    # return Response("Hello, world!", status=200)
    return render_template('ajax_papers_table.html', title='OpenReview Explorer')


@app.route('/api/data')
def data():
    return {'data': [paper.to_dict() for paper in Paper.query]}


@app.route("/custom", methods=["POST"])
def custom():
    payload = request.get_json()

    if payload.get("say_hello") is True:
        output = jsonify({"message": "Hello!"})
    else:
        output = jsonify({"message": "..."})

    return output


@app.route("/health")
def health():
    return Response("OK", status=200)
	
