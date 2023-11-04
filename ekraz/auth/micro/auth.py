#!/usr/bin/env python3
"""
"""
from flask import Blueprint, jsonify, abort, request


from ..models import Auth
from ...mysql import auth_db as db



def signin():

    data = request.get_json()
    if not data:
        abort(404)

    try:
    except Exception:
        return jsonify({"response": "failure"}), 400

