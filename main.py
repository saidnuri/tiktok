from flask import Flask, render_template
import os
from flask import send_from_directory
import requests
app = Flask(__name__)
@app.route('/')
def index2():
    return render_template("index.html", title="Home")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/video/<path:path>')
def snc(path):
    url = "https://tiktok28.p.rapidapi.com/video"
    querystring = {"url": path}
    headers = {
        "X-RapidAPI-Host": "tiktok28.p.rapidapi.com",
        "X-RapidAPI-Key": "529e3f03c0msh06af56ae5d4985dp153eeejsna77eac11e459"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return (response.text)


if __name__ == '__main__':
    app.run()