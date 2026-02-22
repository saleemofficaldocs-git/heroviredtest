from flask import Flask
app = Flask('MyFirst-FlaskApp')
            
@app.route("/")
def Index():
        return "Hello From Flask Application - HeroVired"

app.run(debug=True)
