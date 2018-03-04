#-*- coding: utf-8 -*-

from flask import Flask, request, jsonify

import db_manager
import models
from datetime import datetime

# proto
from Protoc import RspProtocol_pb2
from models import *

#routes를 모아놓은 server.py

app = Flask(__name__)
number = 0

@app.route('/')
def hello_world():
    # add to entry
    #db_manager.db_delete()
    return 'helloww'


@app.route('/login', methods=['POST'])
def login():
    username = get_data('username')
    password = get_data('password')

    _user = db_manager.query(User).filter(User.username == username, User.password == password).first()

    rsp_data = {}
    rsp_data['aaa'] = 'bb'

    if _user is None:
        return jsonify(rsp_data)
    return 'bb'


def get_data(jsonkey):
    return request.form[jsonkey]


if __name__ == '__main__':
    app.run(host='0.0.0.0')



