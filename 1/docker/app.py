from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Tanzu Webinars Demo App is Working! v2'

app.run(host='0.0.0.0', port=5000)