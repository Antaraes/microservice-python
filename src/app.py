from flask import Flask,jsonify,render_template
import socket

app = Flask(__name__)

def fetchHostName():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname),str(ip)

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route("/home")
def index_page():
    hostname,ip = fetchHostName()
    return render_template("index.html",HOSTNAME=hostname,IP=ip)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)