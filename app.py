from flask import Flask
from Housing.logger import logging
from Housing.exception import HousingException
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        raise HousingException(e, sys) from e        logging.info(housing.error_message)
        logging.info("we are testing logging")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)
