from flask import Flask

app = Flask('myfirstapp')

@app.route('/currencyconvertr/<int:dollar>')

def currencyconverter(dollar):

    inr= dollar*92

    return 'dollar in inr: ='+ str(inr)

app.run(debug=True)

