from flask import Flask, render_template

# create app
app = Flask(__name__)

# read file contents
file = open('static/answers.csv')
file.seek(0)
answers = file.readlines()
answers=[entry.strip("\n").split(",") for entry in answers]

@app.route("/results")
def results():
    return render_template('results.html', answers=answers)

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()