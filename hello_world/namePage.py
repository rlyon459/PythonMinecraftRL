from flask import Flask
app = Flask(__name__)

@app.route("/")
def showName():
    return "Dick Dickerson"

app.run()



