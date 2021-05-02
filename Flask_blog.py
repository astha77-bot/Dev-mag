from flask import Flask,render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm

from wtforms.validators import Email
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts=[
    {
      'author':'Daniel',
      'title':'A Gentle Introduction to Generative Adversarial Networks (GANs)',
      'content':'Generative Adversarial Networks are an approach to generative modeling using deep learning methods, such as convolutional neural networks.',
      'date_posted':'February 27,2021'
      },
      {
      'author':'Rebecca',
      'title':'Creativity and artificial intelligence',
      'content':'Creativity is a fundamental feature of human intelligence, and a challenge for AI.',
      'date_posted':'February 26 ,2021'
      }    
    
    ]
@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)