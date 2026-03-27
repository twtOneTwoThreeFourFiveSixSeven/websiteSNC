from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('base.html')

@app.route('/questions', methods=['GET'])
def questions():
    return render_template('questions.html')

if __name__ == '__main__':
    app.run(debug=True)