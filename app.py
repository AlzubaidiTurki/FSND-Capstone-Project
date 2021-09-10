from flask import Flask, json, request, abort, jsonify, redirect
from flask.helpers import url_for
from flask.wrappers import Response
from models import db, Master, Servant, setup_db
from flask_migrate import Migrate
from auth import AuthError, requires_auth
from flask_cors import CORS
import sys

# $env:FLASK_APP=app.py
# $env:FLASK_ENV = "development"

app = Flask(__name__)
setup_db(app)
CORS(app)


class customError(Exception):
    def __init__(self, error):
        self.error = error


@app.route('/')
def index():
    return '<h1> Welcome to the Holy Grail Battle page! </h1> \
    <p> This battle should be a secret to public, \
        you need to login as a master to view other masters and servants \
             :) </p>'


@app.route('/servants', methods=['GET'])
@requires_auth('get:servants')
def get_servants(_):
    servants = Servant.query.all()
    print(servants)
    return jsonify({
        'servants': [servant.format() for servant in servants],
        'success': True
    })


@app.route('/masters', methods=['GET'])
@requires_auth('get:masters')
def get_masters(_):
    # masters = Master.query.all()
    # print(masters)
    return jsonify({
        'masters': [master.format() for master in Master.query.all()],
        'success': True
    })


@app.route('/servants', methods=['POST'])
@requires_auth('post:servants')
def summon_servant(_):

    body = request.get_json()
    print(f'YATA_body {body}')
    if body is None or 'name' not in body:  # name attribute cannot be empty.
        abort(400)

    name = body['name']
    type = body['type'] if 'type' in body else ''
    source = body['source'] if 'source' in body else ''
    image = body['image'] if 'image' in body else ''
    master = None

    try:
        servant = Servant(name=name, type=type, source=source, image=image)
        if 'master' in body:
            master = Master.query.filter_by(name=body['master']).first()
            print(f'MASTER {master}')
            if master is not None:
                servant.master_id = master.id
            else:
                abort(422)

        servant.insert()
    except BaseException:
        db.session.rollback()
        print(f'POST_SERVANT_ERROR {sys.exc_info()}')
        abort(500)

    return jsonify({
        'servants': [servant.format() for servant in Servant.query.all()],
        'success': True
    })
    # return redirect(url_for('get_servants'))


@app.route('/masters', methods=['POST'])
@requires_auth('post:masters')
def assign_master(_):

    body = request.get_json()

    if body is None or 'name' not in body:  # name attribute cannot be empty.
        abort(400)

    name = body['name']
    image = body['image'] if 'image' in body else ''

    try:
        master = Master(name=name, image=image)
        master.insert()
    except BaseException:
        db.session.rollback()
        print(f'POST_MASTER_ERROR {sys.exc_info()}')
        abort(500)

    return jsonify({
        'masters': [master.format() for master in Master.query.all()],
        'success': True
    })

    # return redirect(url_for('get_masters'))


@app.route('/servants/<int:servant_id>', methods=['PATCH'])
@requires_auth('patch:servants')
def update_servant(_, servant_id):
    servant = Servant.query.get(servant_id)
    if servant is None:
        abort(422)
    body = request.get_json()

    if body is None:
        abort(400)

    servant.name = body['name'] if 'name' in body else ''
    servant.type = body['type'] if 'type' in body else ''
    servant.source = body['source'] if 'source' in body else ''
    servant.image = body['image'] if 'image' in body else ''
    master = None
    if 'master' in body:
        master = Master.query.filter_by(name=body['master']).first()
        if master is not None:
            servant.master_id = master.id
        else:
            abort(Response("Master does not exist!"))

    try:
        servant.update()
    except BaseException:
        db.session.rollback()
        print(f'PATCH_SERVANT_ERROR {sys.exc_info()}')
        abort(500)

    return jsonify({
        'servants': [servant.format() for servant in Servant.query.all()],
        'success': True
    })

    # return redirect(url_for('get_servants'))


@app.route('/servants/<int:servant_id>', methods=['DELETE'])
@requires_auth('delete:servants')
def delete_servant(_, servant_id):
    servant = Servant.query.get(servant_id)
    if servant is None:
        abort(422)
    try:
        servant.delete()
    except BaseException:
        db.session.rollback()
        print(f'DELETE_SERVANT_ERROR {sys.exc_info()}')
        abort(500)

    return jsonify({
        'servants': [servant.format() for servant in Servant.query.all()],
        'success': True
    })
    # return redirect(url_for('get_servants'))


@app.route('/masters/<int:master_id>', methods=['DELETE'])
@requires_auth('delete:masters')
def delete_master(_, master_id):
    master = Master.query.get(master_id)
    if master is None:
        abort(422)
    try:
        master.delete()
    except BaseException:
        db.session.rollback()
        print(f'DELETE_MASTER_ERROR {sys.exc_info()}')
        abort(500)

    return jsonify({
        'masters': [master.format() for master in Master.query.all()],
        'success': True
    })
    # return redirect(url_for('get_masters'))


@app.errorhandler(422)
def unprocessable(e):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable Entity."
    }), 422


@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource Not Found."
    }), 404


@app.errorhandler(500)
def not_found(e):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error."
    }), 500


@app.errorhandler(400)
def not_found(e):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request."
    }), 400


@app.errorhandler(AuthError)
def auth_errors(e):
    return jsonify({
        'success': False,
        'error': e.status_code,
        'message': e.error
    }), e.status_code
