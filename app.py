from flask import Flask, render_template, url_for, redirect 


app = Flask(__name__)

# adds routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/coronavirus')
def coronavirus():

    return render_template('coronavirus.html')


@app.route('/family')
def family():
    return render_template('family.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/life')
def life():
    return render_template('life.html')

@app.route('/relationships')
def relationships():
    return render_template('relationships.html')

@app.route('/love')
def love():
    return render_template('love.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/poems')
def poems():
    return render_template('poems.html')

if __name__ == '__main__':
    app.run(debug=True)
