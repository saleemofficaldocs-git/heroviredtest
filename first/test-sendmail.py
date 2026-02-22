from flask import Flask
app = Flask('myapp')
            
@app.route("/sendEmail")
def sendEmailToClient():
        return "Email Sent Successfully"

@app.route("/log/<msg>")
def log(msg):
        return 'Info: Your Log ' + msg +" is recorded"

@app.route("/showBlog/<int:postID>")
def showBlog(postID):
        return 'Showing Blog with Post ID '+ str(postID)

app.run(debug=True)

