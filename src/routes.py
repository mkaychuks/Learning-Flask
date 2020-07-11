from src import app, bcrypt, db

from flask import(
    render_template, url_for, flash, redirect
)


from src.models import User, Post
from src.forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Ifeanyi',
        'title': 'Blog post 1',
        'content': 'First Post content',
        'date_created': 'April 20, 2018'
    },
    {
        'author': 'Ifeanyi A',
        'title': 'Blog post 2',
        'content': 'Second Post content',
        'date_created': 'April 30, 2018'
    },
    {
        'author': 'Ifeanyi Achufusi',
        'title': 'Blog post 3',
        'content': 'Third Post content',
        'date_created': 'April 22, 2018'
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


# creating a Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Accoutn Registration Successful, You are now able to login!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



# creating a Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'testing':
            flash('Successfully Logged-In', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed, check username or passowrd', 'danger')
    return render_template('login.html', title='Login', form=form)