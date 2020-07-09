from flask import(
    Flask, render_template, url_for, flash, redirect
)
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime


from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '23d482aeed3777bb905174a9c5097b32' # setting our secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # part to our database
db = SQLAlchemy(app) # sqlalchemy instance


# user class model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# post class model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"



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
        flash(f'Accounted created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
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




if __name__ == '__main__':
    app.run(debug=True)

