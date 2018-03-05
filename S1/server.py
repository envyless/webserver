#-*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import random

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
    db_manager.db_flush()
    username = get_data('username')
    password = get_data('password')

    _user = db_manager.query(User).filter(User.username == username, User.password == password).first()

    rsp_data = {}

    if _user is None:
        rsp_data['result'] = 'failed'
    else:
        rsp_data['result'] = 'succes'
        rsp_data['money'] = _user.money;
        rsp_data['username'] = _user.username;
        print "monsey : ", _user.money

    db_manager.db_flush()
    return jsonify(rsp_data)


@app.route('/join', methods=['POST'])
def join():
    username = get_data('username')
    password = get_data('password')

    rsp_data = {}
    if username is None or len(username) == 0:
        return jsonify(rsp_data)

    if password is None or len(password) == 0:
        return jsonify(rsp_data)

    rsp_data['result'] = 'succes'

    _user = db_manager.query(User).filter(User.username == username).first()

    if _user is None:
        rsp_data['result'] = 'succes'
        _user = User()
        _user.username = username
        _user.password = password
        _user.money = 50000
        db_manager.db_session.add(_user)
        db_manager.db_commit()
        rsp_data['money'] = _user.money
        rsp_data['username'] = username
        rsp_data['password'] = password

    else:
        rsp_data['result'] = 'failed'

    return jsonify(rsp_data)


@app.route('/batting_start', methods=['POST'])
def batting_start():
    db_manager.db_flush()
    username = get_data('username')
    batting_money = get_data('money')

    if batting_money is None:
        return "no money"

    _user = db_manager.query(User).filter(User.username == username).first()

    if _user is None:
        return "user is none"

    master_num = random.randrange(1, 100)
    user_num = random.randrange(1, 100)
                        
    rsp_data = {}
    rsp_data['master_num'] = master_num
    rsp_data['user_num'] = user_num

    print "old money : ", _user.money 

    if master_num < user_num:
        _user.money = _user.money + int(batting_money)
        rsp_data['result'] = 'succes'
    else:
        _user.money = _user.money - int(batting_money)
        rsp_data['result'] = 'failed'

    print "new money : ", _user.money
    
    #db_manager.db_commit()
    rsp_data['money'] = _user.money
    db_manager.db_commit()
    return jsonify(rsp_data)


def get_data(jsonkey):
    return request.form[jsonkey]


if __name__ == '__main__':
    app.run(host='0.0.0.0')



