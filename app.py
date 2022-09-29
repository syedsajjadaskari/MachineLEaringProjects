from crypt import methods
from distutils.log import debug
from flask import Flask
app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    return "Starting machine learing Projects"

if __name__=="__main__":
    app.run(debug=True)