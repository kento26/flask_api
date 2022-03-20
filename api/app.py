from flask import Flask, jsonify, request
from pykakasi import kakasi
from functools import reduce
import json

app = Flask(__name__)
kakasi = kakasi()

@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)

    kakasi.setMode('H', 'a')
    kakasi.setMode('K', 'a')
    kakasi.setMode('J', 'a')
    conv = kakasi.getConverter()

    result = map(lambda e: {
        'postID': e['post_id'],
        'jp': e['summary'],
        'rome': list(map(lambda o: conv.do(o) ,e['summary']))
      } ,data)

    return jsonify(list(result))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)