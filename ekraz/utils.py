#!/usr/bin/env python3
"""
"""
from typing import List, Union, Tuple, Dict


from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from passlib.hash import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()


def encrypt(password: str) -> str:
    return generate_password_hash(password=password, method=bcrypt.using(rounds=12))


def decrypt(password: str, new_password: str) -> bool:
    return check_password_hash(password, new_password)


def into(attr, data: Union[List, Tuple, str]) -> bool:

    if type(data) is str:
        if type(attr) != str:
            return False

    return True if attr in data else False


def typeof(attr, datatype: Union[List, Tuple]) -> bool:
    
    return True if type(attr) in datatype else False


def sizeof(attr: Union[List, Dict, Tuple, str], size: int) -> bool:

    return True if len(attr) >= size else False


def image_ext(filename: str):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'png'


def uploading(file: str) -> str:

    if image_ext(file.filename):

        filename = secure_filename(file.filename)
        file.save(os.path.join(os.environ.get('UPLOAD_FOLDER')), filename)

        return filename

    return os.path.join(os.path.abspath('/ekraz/uploads'), 'nouser.png')


def init_session(session):

    # initialisation du nombre de tentative de connexion 0 avec 5 pour max
    # apres 5 tantative rater le compte est desactiver pour 5 min + 5 * __compte_temporary_blocked__
    session['__connexion_attempt__'] = 0

    # initialisation du nombre de fois les 5 tantative sont possible a zero avec 3 comme max
    # apres chaque tour envoie d'email a l'utilisateur pour informr d'intrusion dans sont compte
    # et envoie d'un code de verification a validiter de 10 min pour attester son identiter et modifier ces infos de connexion
    # apres les 3 tours desactivation du compte alors __compte_temporary_blocked__ = -1
    # et envoie de mail a utilisateur pour reactivation du compte
    session['__compte_temporary_blocked__'] = 0

    pass


def profilserializer(profil) -> Dict[str, Any]:

    data = {
        'username': profil.username,
        'firstname': profil.firstname,
        'genre': profil.genre,
        'phone': profil.phone,
        'country': profil.country,
        'job': profil.job,
        'about': profil.about,
        'email': profil.email,
        'picture': profil.picture,
        'github': profil.github,
        'gitlab': profil.gitlab,
        'twitter': profil.twitter,
        'linkedin': profil.linkedin,
        'website': profil.website,
        'experience': [
            {
                'title': exp.title,
                'start': exp.start,
                'end': exp.end,
                'description': exp.description
            }
            for exp in profil.experiences
        ],
        'formations': [
            {
                'title': form.title,
                'start': form.start,
                'end': form.end,
                'where': form.where,
                'link': form.link,
                'description': form.description
            }
            for form in profil.formations
        ],
        'languages': [
            {
                'lang': lg.lang,
                'year': ld.year
            }
            for lg in profil.languages
        ],
        'abonnements': [
            {
                'name': ab.name,
                'duration': ab.duration
            }
            for ab in profil.abonnements
        ]
    }

    return data


def expserializer(exp):

    data = {
        'title': exp.title,
        'start': exp.start,
        'end': exp.end,
        'description': exp.description
    }

    return data




