from flask import Flask, render_template

app = Flask('myapp')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/ourservices")
def service():
    username='Herovired'
    return render_template('services.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')





app.run(debug=True)
