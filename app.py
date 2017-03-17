#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Sample project to test REST API using flask framework.
'''
__version__ = 'v0.0.0'
__author__ = 'Vishnu G'

from flask import Flask,jsonify
from flask_restful import Resource
from flask_restful import reqparse
from flask import render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/db'
mongo = PyMongo(app)


api = {"name" : "Sample Flask Project API", "version" : "v0.0.0", "status" : "All APIs are working fine"}

@app.route("/api", methods=['GET'])
def api_test():
    return jsonify(api)

@app.route("/mongotest", methods=['GET'])
def mongo_test():
    try:
        test = mongo.db.test
        output = []
        
        for q in test.find():
            output.append({"project" : q['project']})

        return jsonify({'StatusCode':'200','data':output})
    except Exception as e:
        return jsonify({'error': str(e)}) 

@app.route("/index", methods=['GET'])
def get_invoice():
    try:
        
        pos_items = {"project" : api.get("name"), "version" : api.get("version")}
        return render_template('index.html',
                    title='Home',
                    pos_items=pos_items)
    except Exception as e:
        return jsonify({'error': str(e)}) 

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'StatusCode':'200','msg':'test api'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)
