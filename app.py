from flask import Flask, render_template


app = Flask(__name__)

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
def homePage():
    return render_template('home.html', posts=posts)


@app.route('/about')
def aboutPage():
    return render_template('about.html', title='About') 


if __name__ == '__main__':
    app.run(debug=True)

