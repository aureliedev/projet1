from flask import Flask, jsonify, request
import json

app = Flask(__name__)

booking_list = []

class booking:
  def __init__(self, room):
        self.room = room

@app.route('/')
def index():
  return 'Index, API is running'

@app.route('/booking', methods=['GET', 'POST'])
def booking_get_post():
  if (request.method == 'GET'):
    return jsonify(booking_list)
  if (request.method == 'POST'):
    room = request.get_json(['room'])
    booking_list.append(booking(room))
    return jsonify(booking_list)
  return

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8000)