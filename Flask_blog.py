from flask import Flask,render_template 
app = Flask(__name__)

posts=[
    {
      'author':'astha vijayvargiya',
      'title':'Blog post 1',
      'content':'First post content',
      'date_posted':'February 27,2021'
      },
      {
      'author':'aditya vijayvargiya',
      'title':'Blog post 2',
      'content':'Second post content',
      'date_posted':'February 27 ,2021'
      }    
    
    ]
@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    run_simple('localhost', 5000, app,use_reloader=True, use_debugger=True, use_evalex=True)
