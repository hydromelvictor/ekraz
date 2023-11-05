#!/usr/bin/env python3
"""
"""
from flask import Blueprint, jsonify, abort, request
import phonenumbers
from ...utils import expserializer


from ..models import Experience
from ...mysql import profil_db as db



# cree
def create():

    data = request.get_json()
    if not data:
        abort(404)

    if 'description' in data.keys():
        if len(data['description']) > 250:
            return jsonify({'message': '500 words only'})
    
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
        experiences = [
            exp.datadic for exp in db.session.execute(db.select(Experience)\
                                                       .order_by(Experience.end))\
                                                       .scalars().all()
        ]

        return jsonify({
            'message': 'Success',
            'data': experiences
        }), 200
    
    except Exception:
        return jsonify({'message': 'failure'}), 400


def filter_by():

    data = request.get_json()
    if not data:
        abort(404)

    try:
        experiences = [
            ex.datadict for exp in db.session.execute(db.select(Experience)\
                                                      .filter_by(**data)\
                                                      .order_by(Experience.end))\
                                                      .scalars()\
                                                      .all()
        ]

        return jsonify({
            'message': 'Success',
            'data': experiences
        }), 200
    
    except Exception:
        return jsonify({'message': 'failure'}), 400


def get(id):

    try:
        experiences = [
            exp.db.session.execute(db.select(Experience).filter_by(id=id)).scalar()

        return jsonify({
            'message': 'SUccess',
            'data': exp
        })
    
    except Exception:
        return jsonify({'message': 'failure'}), 400

# delete

# update
