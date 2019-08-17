from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)   # __name__ is equal to __main__

# use Python to get the random bytes: import secrets --> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'a0b645caee78ca9c9c5f920ca7980c67'

# set up dummy variables (posts)
posts = [
    {
        'author': 'Stefan Brunotte',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 13, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 14, 2019'
    }
]


@app.route("/")         # / is the root (or home) page of the web page
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")         # / is the root/about page of the web page
def about():
    return render_template('about.html', title='About')


# / using the RegistrationForm
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # see get_flash_messages in flaskblog.py
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])         # / using the LoginForm
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':  # if we run the app in Python this statement is triggered
    app.run(debug=True)
