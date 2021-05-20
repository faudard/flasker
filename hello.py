from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

#def index():
#   return "<h1>Hello World!</h1>"
#safe        => html 
#capitalize
#lower
#upper
#title
#trim 
#striptags

def index():
   first_name = "John"
   stuff = "This is <strong>Bold</strong> Text"
   favorite_pizza=["Pepperoni","cheeze","Mushrooms", 41]
   return render_template("index.html", 
     first_name=first_name, 
     stuff=stuff,
     favorite_pizza=favorite_pizza)
# Flask recognize the location templates of the index.html 


# localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
   #return "<h1>Hello {}!!!</h1>".format(name)
   return render_template("user.html", user_name=name)


# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Invalid Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

#if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=5000)
    #a#pp.run(host='0.0.0.0')



