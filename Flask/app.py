from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    posts = [{'title': 'First Post', 'created': '2020-05-01'}, 
             {'title': 'Second Post', 'created': '2020-05-02'}]
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    posts = [{'title': 'About me', 'created': '2020-05-01'}, 
             {'title': 'About you', 'created': '2020-05-02'}]
    return render_template('about.html', posts=posts)


@app.route('/users')
def users():
    file = open('Flask/static/users.json')
    users = json.load(file)
    for user in users:
        print(users[user])
    return render_template('users.html', users=users)

if __name__ == "__main__":
    app.run()