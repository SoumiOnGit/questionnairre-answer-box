from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('show_hide_answer.html')

if __name__ == '__main__':
    app.run(debug=True)