from flask import Flask,render_template
app = Flask(__name__)

posts = [
    {
        'author':'denooo',
        'title' : 'post1',
        'content':'i am awesome',
        'date_posted':'April20,2018'
    },
    {
        'author':'maina',
        'title' : 'post2',
        'content':'i am awesome 2', 
        'date_posted':'April 20,2018'   
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title= 'About')


if __name__ == '__main__':
    app.run(debug=True)
