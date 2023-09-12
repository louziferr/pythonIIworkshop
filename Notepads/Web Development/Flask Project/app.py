from flask import Flask, render_template

# create app
app = Flask(__name__)

# open file with data
file = open('static/answers.csv')

# read file
lines = file.readlines()

# reformat answers and save in list
answers= [ entry.strip("\n").split(",") for entry in lines ]

# route for showing results
@app.route("/results")
def results():
    return render_template('results.html', answers=answers)

# route for start page
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()