from flask import Flask, render_template
import requests

posts = requests.get('https://api.npoint.io/94b853fbe051632b1847').json()


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', all_posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for individual_posts in posts:
        if individual_posts["id"] == index:
            requested_post = individual_posts
    return render_template("post.html", id_post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)