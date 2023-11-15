from flask import Flask, render_template, request, redirect, url_for
from stanfordcorenlp import StanfordCoreNLP
import logging
import json


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


nlp = StanfordCoreNLP('http://nlproject', port=9000)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form submissions here
    message = request.form['inputMessage']

    # Perform server-side validation
    if not message:
        return "All fields are required. Please fill in all the fields."

    if message.count('.') < 1:
        return "The Message field must contain at least one sentence."

    # Process the text using Stanford CoreNLP
    result = nlp.annotate(message, properties={
        'annotators': 'tokenize,ssplit,pos',
        'outputFormat': 'json'
    })

    json_result = json.loads(result)

    # app.logger.info(f"Result: {json_result}")

    app.logger.info(f"Result type: {type(json_result)}")  # Print the data type


    nlp.close()

    # Render the result in a table format
    return render_template('output.html', result=json_result, message = message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000