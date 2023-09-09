from flask import Flask, render_template, request, url_for, flash, redirect
import json

# create app
app = Flask(__name__)
app.config['SECRET_KEY'] = '3efj38d92dfjeke284fdj394urjf93j9fu4f84j9d'

# read file
question_file = open('Flask/questionnaire/static/questions.json')
questions = json.load(question_file)
question_file.close()

# get attributes
attributes = [questions[question]['title'] for question in questions]

# list of answers
answers=[]

# open file to read and save answers
answer_file = open("Flask/questionnaire/static/answers.txt", "a+")

# start reading from the beginning
answer_file.seek(0)
# iterate over answers
for line in answer_file:
    # append answers to list
    answers.append(line.strip("\n").split("\t"))

## APP ROUTING ##

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questionnaire', methods=('GET', 'POST'))
def questionnaire():
    if request.method == 'POST':
        # check if form is filled out correctly
        missing = missing_attribute(request.form)
        if missing:
            flash(missing + " is missing!")
        else:
            # save answer
            save_answer(request.form)
            return redirect(url_for('results'))
    return render_template('questions.html', questions=questions)

@app.route('/results')
def results():
    return render_template('results.html', results=answers)

## HELPER FUNCTIONS ##

# check if request form is filled out correctly
def missing_attribute(request_form):
    for attribute in attributes:
        if not request_form[attribute]:
            return attribute

# save new answer
def save_answer(answer):
    # create list of answered attributes
    answer_list = [answer[attribute] for attribute in attributes]
    # append to current answer list
    answers.append(answer_list)
    # write to file
    answer_file.write("\t".join(answer_list))
    answer_file.write("\n")

if __name__ == "__main__":
    app.run()