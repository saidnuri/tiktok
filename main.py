from flask import Flask, render_template
import os
from flask import send_from_directory
import requests
import json

app = Flask(__name__)
@app.route('/')
def index2():
    return render_template("index.html", title="Home")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/video/<path:path>')
def snc(path):
    id=path.split("/video/")[1].split("?")[0]
    
    url = "https://tiktok-all-in-one.p.rapidapi.com/video"

    querystring = {"id":id}

    headers = {
	"X-RapidAPI-Host": "tiktok-all-in-one.p.rapidapi.com",
	"X-RapidAPI-Key": "529e3f03c0msh06af56ae5d4985dp153eeejsna77eac11e459"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    sonuc=json.loads(response.text) 
    return (str(sonuc.get("aweme_details")))


if __name__ == '__main__':
    app.run()