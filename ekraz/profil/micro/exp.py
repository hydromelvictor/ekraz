#!/usr/bin/env python3
"""
"""
from flask import Blueprint, jsonify, abort, request
import phonenumbers


from ..models import Experience
from ...mysql import profil_db as db



# cree
def create():

    data = request.get_json()
    if not data:
        abort(404)
    
    try:
        exp = Experience(**data)
        db.session.add(exp)
        db.session.commit()

        return jsonify(
            {
                'message': 'Success',
                'data': exp.datadict
            }
        ), 201
    
    except Exception:
        return jsonify({'message': 'failure'}), 400


# lister
def all():

    try:
        experiences = db.session.execute(db.select(Experience).order_by(Experience.Profil.username)).scalars().all()
# experience specifique

# delete

# update
