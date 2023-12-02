from flask import Flask ,render_template,url_for
app = Flask(__name__)  #it is special variable in python that is just name of the module

posts = [
    {
        "author" : 'saurav',
        'title' : "blog post 1",
        'content' : 'first post content',
        'date_posted' : 'april 20,2018'
    },
    {
        "author" : 'kurian',
        'title' : "blog post 2",
        'content' : 'second post content',
        'date_posted' : 'april 21,2018'
    }
    
]

@app.route("/")#will handle all the backend stuff
@app.route("/home")
def hello():
    return render_template('home.html',posts = posts)
@app.route("/about") #will handle all the backend stuff
def about():
    return render_template('about.html',title = 'about')




if __name__ == "__main":
    app.run(debug =True) ##__name is main if run python directly but if we import it somewehere else the __name__ will be module