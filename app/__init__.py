from flask import Flask       # from the flask "module" import the Flask "class"


app = Flask(__name__)         # Initialize or instantiate the Flask class into the app variable 
                              # app is an object(an instance of the Flask class)
                              # The relationship between objects and classes is like the
                              # relationship between houses and their blueprints 



@app.route("/")               # Flask decorator that maps a route to a view funtion 
def about_me():               # view function
                              # A dictionary type variable called "me"
    me = {                    
        "first_name": "Nicholas",   # <- key/value pairs for our dictionary
        "last_name": "GPL",
        "hobbies": "DIY stuff",
        "active": True
    }

@app.route("/greet/<fname>/<lname>")
def greet_user(fname,lname):
    return "<h1>Hello,%s %s</h1>" % (fname,lname)