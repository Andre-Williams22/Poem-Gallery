from flask import Flask, render_template, url_for, redirect 


app = Flask(__name__)

# adds routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/poems')
def poems():
    return render_template('poems.html')

if __name__ == '__main__':
    app.run(debug=True)
