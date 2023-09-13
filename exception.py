from flask import Flask
from Fraud_Transaction_Detection.logger import logging
from Fraud_Transaction_Detection.exception import BankingException
import os, sys


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    try:
        raise Exception("Exception file tester...")
    except Exception as e:
        ML = BankingException(e, sys)
        logging.info(ML.error_message)


    logging.info("Logging file tester...")
    return "Testing Successful"

if __name__ == '__main__':
    app.run(debug=True)