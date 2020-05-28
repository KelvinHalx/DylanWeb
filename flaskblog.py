from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']= '5e2d6f337a3d5e3202aa1a996eb6b523'

posts =[
    {
        'author': 'Kelvin Halx',
        'title':'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'May 19th,2020',
    },
    {
        'author': 'Dylan Wainaina',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'May 20th, 2020',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for{form.username.data}!','sucess')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You have been logged in!','sucess')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)

