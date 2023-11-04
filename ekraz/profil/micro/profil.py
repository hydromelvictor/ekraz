#!/usr/bin/env python3
"""
"""
from flask import jsonify, abort, request
import phonenumbers


from ..models import Profil
from ...mysql import profil_db as db
from ...utils import encrypt


mark = '.,;|/\?<>:!*$^'
# cree un profil
# cette function est celle executer avant l'autentification
# nous creons l'utilisateur ensuite l'authentifions
# dans l'authentification 
# username = profil.id
# password = profil.password
def create():
    
    data = request.get_json()
    if not data:
        abort(404)
    
    # les elements requis sont username et password
    if not data['username']:
        return jsonify({'message': 'username required'}), 400
    
    if type(data['username']) is not str:
        return jsonify({'message': 'string required'}), 400
    
    if len(data['username']) < 4:
        return jsonify({'message': "username must be greater than 4"}), 400
    
    if not all(c not in mark for c in data['unsername']):
        return jsonify({'message': f"these charaters {mark.split(', ')} not authorize in the username"})
    
    if db.session.execute(db.select(Profil).filter_by(username=data['username'])).scalars().first():
        return jsonify({'message': f"sorry, {data['username']} exists]"})
    
    if not data['password']:
        return jsonify({'message': 'password required'}), 400
    
    if type(data['password']) is not str:
        return jsonify({'message': 'string required'}), 400
    
    if len(data['password']) < 8:
        return jsonify({'message': "password must be greater than 8"}), 400
    
    if not data['email']:
        return jsonify({'message': 'email required'}), 400

    if type(data['email']) is not str:
        return jsonify({'message': 'string required'}), 400

    if len(data['email']) < 1 or '@' not in data['email']:
        return jsonify({'message': 'insuffisance characters'}), 400
    
    if db.session.execute(db.select(Profil).filter_by(email=data['email'])).scalars().first():
        return jsonify({'message': f"sorry, {data['email']} exists]"})
    
    try:
        data['password'] = encrypt(data['password'])
        profil = Profil(**data)
        db.session.add(profil)
        db.session.commit()

        # authentification

        # session

        return jsonify(
            {
                'message': 'Success',
                'data': profil.datadict
            }), 201

    except Exception:
        return jsonify({'message': 'failure'}), 400


# lister tout les profil
def all():
    
    try:
        users = db.session.execute(db.select(Profil).filter_by(active=True).order_by(Profil.username)).scalars().all()
        
        return jsonify(
            {
                'message': 'Success',
                'data': users
            }
        ), 200
    
    except Exception:
        return jsonify({'message': 'failure'}), 400


# trouver un profil par son id
def get(id):
    
    user = db.one_or_404(db.select(Profil).filter_by(id=id, active=True))

    if user:
        return jsonify(
            {
                'message': 'Success',
                'data': user.datadict
            }
        )

    else:
        return jsonify({'message': 'failure'}), 400


# lister des profil specifique
def filter_by():

    data = request.get_json()
    if not data:
        abort(404)
    
    data['active'] = True
    try:
        users = db.session.execute(db.select(Profil).filter_by(**data).order_by(Profil.username)).scalars().all()

        return jsonify(
            {
                'message': 'Success',
                'data': users
            }
        ), 200
    
    except Exception:
        return jsonify({'respnse': 'failure'}), 400


# supprimer un profil
def delete(id):
    
    try:
        user = db.one_or_404(db.select(Profil).filter_by(id=id, active=True))
        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'Success'}), 200
    
    except Exception:
        return jsonify({'message': 'failure'}), 400



# lister tout les profil desactiver
def deactivated():
    
    try:
        users = db.session.execute(db.select(Profil).filter_by(active=False).order_by(Profil.username)).scalars().all()
        
        return jsonify(
            {
                'message': 'Success',
                'data': users
            }
        ), 200
    
    except Exception:
        return jsonify({'message': 'failure'}), 400



# mis a jour d'un profil
def update(id):
    
    data = request.get_json()
    if not data:
        abort(404)
    
    user = db.one_or_404(db.select(Profil).filter_by(id=id, active=True))

    user.username = data['username']
    user.firstname = data['firstname']
    user.lastname = data['lastname']
    user.genre = data['genre']
    
    phone = phonenumbers.parse(data['phone'])

    if phonenumbers.is_valid_number(phone):

        user.phone = phone
        user.country = phonenumbers.geocoder.description_for_number(phone)
    
    else:
        return jsonify({'message': 'phone not valid'}), 400
    
    user.job = data['job']
    user.about = data['about']
    user.email = data['email']

    picture = request.files['picture']

    user.github = data['github']
    user.gitlab = data['gitlab']
    user.twitter = data['twiter']
    user.linkedin = data['linkedin']
    user.website = data['website']

    try:
        db.session.commit()
        return jsonify(
            {
                'mesasage': 'Success'
            }
        ), 200

    except Exception:
        return jsonify({'message': 'failure'}), 400


