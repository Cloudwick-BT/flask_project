from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!, I am back!"
@app.route("/user")
def user():
    return "Hello User !"

if __name__ == "__main__":
    app.run(debug = True) # it reloads the website if change is detected.
