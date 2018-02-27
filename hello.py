from flask import Flask
from flask import json,jsonify
from flask import request

app = Flask(__name__)
users=[
        {
         'id' : 0,
         'name':''  
        }   
      ]
@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def new_users():
    input=request.get_json(force=True)
    user={
            'id': users[-1]['id'] + 1,
            'name': input['name']
          }
    users.append(user)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    users.remove(user[0])
    return jsonify(),204
        
        