import os
from flask import Flask


app = Flask(__name__)

@app.route('/hostname', methods=['GET'])
def get_hostname():
    return os.uname().nodename

@app.route('/author', methods=['GET'])
def get_author():
    return os.environ.get('AUTHOR', 'Unknown')

@app.route('/id', methods=['GET'])
def get_id():
    return os.environ.get('UID', 'Unknown')

@app.errorhandler(404)
def pageNotFount(error):
    return "Not found"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
