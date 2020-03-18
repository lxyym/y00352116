import os

app = Flask(__name__)

@app.route.('/')

def show_hostname():
    html = "<h2>The hostname is : {hostname}</h2>"
    return html.format(hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
