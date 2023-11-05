#!/usr/bin/env python3
"""
"""
from flask import jsonify, abort, request, session
import phonenumbers


from ..models import Profil
from ...mysql import profil_db as db
from ...utils import (
    encrypt,
    into,
    typeof,
    sizeof,
    uploading,
    profilserializer
)

mark = '.,;|/\?<>:!*$^\'"'
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
    _attrs = data.keys()
    
    if not into('username', _attrs):
        return jsonify({'message': 'username required'}), 400
    
    if not typeof(data['username'], (str)):
        return jsonify({'message': 'string required'}), 400
    
    if not sizeof(data['username'], 4):
        return jsonify({'message': "username must be greater than 3"}), 400
    
    if not all( into(c, mark) for c in data['username']):
        return jsonify({'message': f"these charaters {mark.split(', ')} not authorize in the username"})
    
    try:
        if db.session.execute(db.select(Profil).filter_by(username=data['username'])).scalars().first():
            return jsonify({'message': f"sorry, {data['username']} exists]"})
    
    except Exception:
        return jsonify({'message': 'failure'}), 400
    
    if not into('password', _attrs):
        return jsonify({'message': 'password required'}), 400
    
    if not typeof(data['password'], (str)):
        return jsonify({'message': 'string required'}), 400
    
    if not sizeof(data['password'], 6):
        return jsonify({'message': "password must be greater than 5"}), 400
    
    if not into('email', _attrs):
        return jsonify({'message': 'email required'}), 400

    if not typeof(data['email'], (str)):
        return jsonify({'message': 'string required'}), 400

    if not sizeof(data['email'], 8) or '@' not in data['email']:
        return jsonify({'message': 'insuffisance characters'}), 400
    
    try:
        if db.session.execute(db.select(Profil).filter_by(email=data['email'])).scalars().first():
            return jsonify({'message': f"sorry, {data['email']} exists]"})
    
    except Exception:
        return jsonify({'message': 'failure'}), 400
    

    try:
        data['password'] = encrypt(data['password'])
        profil = Profil(**data)
        db.session.add(profil)
        db.session.commit()

        # authentification et login par jwt

        session['__compte_blocked__'] = 0
        session['__compte_blocked_count__'] = 0

        session['_user_'] = {
            'id': profil.datadict['id'],
            'username': profil.datadict['username'],
            'email': profil.datadict['email']
        }

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
        users = [ 
            profilserializer(user) for user in db.session.execute(db.select(Profil)\
                                                         .filter_by(active=True)\
                                                         .order_by(Profil.username))\
                                                         .scalars().all()
        ]
        
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
    
    try:
        user = db.session.execute(db.select(Profil).filter_by(id=id, active=True)).scalar()

        if user:
            return jsonify(
                {
                    'message': 'Success',
                    'data': profilserializer(user)
                }
            ), 200

        else:
            return jsonify({'message': f"{id} unknown"}), 404
    
    except Exception:
        return jsonify({'message': 'failure'}), 400

# lister des profil specifique
def filter_by():

    data = request.get_json()
    if not data:
        abort(404)
    
    data['active'] = True
    try:
        users = [
            profilserializer(user) for user in db.session.execute(db.select(Profil)\
                                                                   .filter_by(**data)\
                                                                   .order_by(Profil.username))\
                                                                   .scalars().all()
        ]

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
        user = db.session.execute(db.select(Profil).filter_by(id=id, active=True)).scalar()

        if user:
            user.active = False
            db.session.commit()

            return jsonify({'message': 'Success'}), 200
        else:
            return jsonify({'message': f"{id} unknown"}), 404
    
    except Exception:
        return jsonify({'message': 'failure'}), 400



# lister tout les profil desactiver
def deactivated():
    
    try:
        users = [
            profilserializer(user) for user in db.session.execute(db.select(Profil)\
                                                         .filter_by(active=False)\
                                                         .order_by(Profil.username))\
                                                         .scalars().all()
        ]
        
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
    
    try:
        user = db.session.execute(db.select(Profil).filter_by(id=id, active=True)).scalar()

        _attrs = data.keys()

        username = user.username
        user.username = data['username'] if into('username', _attrs) and\
            typeof(data['usrname'], (str)) and sizeof(data['username'], 4) else ''
    
        if user.username == '':
            user.username = username
    
        user.firstname = data['firstname'] if into('firstname', _attrs) and typeof(data['firstname'], (str)) else ''
        user.lastname = data['lastname'] if into('lastname', _attrs) and typeof(data['lastname'], (str)) else ''
        user.genre = data['genre'] if into('genre', _attrs) and typeof(data['genre'], (str)) else ''

        phone = phonenumbers.parse(data['phone']) if into('phone', _attrs) and typeof(data['phone'], (str)) else ''

        if phonenumbers.is_valid_number(phone):

            user.phone = phone
            user.country = phonenumbers.geocoder.description_for_number(phone)

        else:
            return jsonify({'message': 'phone not valid'}), 400

        user.job = data['job'] if into('jod', _attrs) and typeof(data['jod'], (str)) else ''
        user.about = data['about'] if into('about', _attrs) and typeof(data['about'], (str)) and len(data['about']) < 5001 else ''
        user.email = data['email'] if into('email', _attrs) and typeof(data['email'], (str)) and '@' in data['email'] else ''

        file = request.files['picture'] if into('picture', _attrs) and typeof(data['picture'], (str)) and sizeof(data['picture'], 3) else ''

        user.picture = uploading(file)


        user.github = data['github'] if into('github', _attrs) and typeof(data['github'], (str)) else ''
        user.gitlab = data['gitlab'] if into('gitlab', _attrs) and typeof(data['gitlab'], (str)) else ''
        user.twitter = data['twiter'] if into('twitter', _attrs) and typeof(data['twitter'], (str)) else ''
        user.linkedin = data['linkedin'] if into('linkedin', _attrs) and typeof(data['linkedin'], (str)) else ''
        user.website = data['website'] if into('website', _attrs) and typeof(data['website'], (str)) else ''

        db.session.commit()

        session['_user_'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

        return jsonify(
            {
                'mesasage': 'Success'
            }
        ), 200

    except Exception:
        return jsonify({'message': 'failure'}), 400


def reset_password(id):

    data = request.get_json()
    if not data:
        abort(404)
    
    try:
        user = db.session.execute(db.select(Profil).filter_by(id=id, active=True)).scalar()

        if user:
            old = data['old_password']
            new = data['new_password']
            confirm = data['confirm_password']

            if session['__compte_blocked__'] == 5:
                session['__compte_blocked__'] == -1
                # debloquer le compte apres 5 min + 5 * le nombre de fois __compte_blocked_count__
                user.active = False

            if old == user.password:

                if new == confirm:
                    user.password = encrypt(new)
                    db.session.commit()

                    # logout

                else:
                    return jsonify({'message': 'confirmation failure'}), 400
            else:
                session['__compte_blocked__'] += 1
                return jsonify({'message': f"old password not corret, {5 - session['__compte_blocked__']} tentadive before blocked"})

        else:
            return jsonify({'message': f'not usr with id={id} exists'})

    except Exception:
        return jsonify({'message': 'failure'}), 400
