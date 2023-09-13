from flask import Flask
from Fraud_Transaction_Detection.logger import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("Logging file tester...")
    return "Testing Successful"

if __name__ == '__main__':
    app.run(debug=True)