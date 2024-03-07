# Importing Libraries
from flask import Flask

# Setting up the Flask application
app = Flask(__name__)

# Creating a route for the default URL
@app.route("/")
def index():
    return "Hello World!"

# Running the Flask application
if __name__ == "__main__":
    app.run(debug=True)