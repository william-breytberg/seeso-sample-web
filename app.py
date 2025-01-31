from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100), unique=True, nullable=False)
    correct_answer = db.Column(db.String(50), unique=True, nullable=False)
    w1_answer = db.Column(db.String(50), unique=True, nullable=False)
    w2_answer = db.Column(db.String(50), unique=True, nullable=False)
    w3_answer = db.Column(db.String(50), unique=True, nullable=False)
    subject = db.Column(db.String(50), unique=False, nullable=False)
    
    def repr(self):
        return '<Questions %r>' % self.id
    
    # def getquestion(request):
    #     return 


@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/questions")
def questions():
    return render_template('quiz_page.html')

@app.route("/instructions")
def instructions():
    return render_template('instructions.html')

@app.route("/results")
def results():
    return render_template('results.html')

@app.route("/answers")
def answers():
    return render_template('answers.html')

if __name__ == "__main__":
    app.run(debug=True)