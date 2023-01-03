from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get('https://api.npoint.io/94b853fbe051632b1847').json()
USER = "letov88@gmail.com"
PASSWORD = "passwod"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', all_posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(from_addr=USER,
                                to_addrs=USER,
                                msg="Subject:New Message!\n\n"
                                    f"Name: {data['name']}\n"
                                    f"Email: {data['email']}\n"
                                    f"Phone: {data['phone']}\n"
                                    f"\nMessage: \n{data['message']}")

        return render_template('contact.html')
    else:
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
