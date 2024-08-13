from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the service page
@app.route('/services')
def services():
    return render_template('services.html')

# You can add more routes here for additional pages

if __name__ == '__main__':
    app.run(debug=True)
