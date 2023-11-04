#!/usr/bin/env python3
"""
"""
from flask import Blueprint

from .profil.micro import profil


route = Blueprint('route', __name__)

subdomain = ''


# profil
route.add_url_rule(rule='/profil/create', view_func=profil.create, methods=['POST'], strict_slashes=False)
route.add_url_rule(rule='/profil/users', view_func=profil.all, methods=['GET'], strict_slashes=False)
route.add_url_rule(rule='/profil/<id>', view_func=profil.get, methods=['GET'], strict_slashes=False)
route.add_url_rule(rule='/profil/filter', view_func=profil.filter_by, methods=['GET'], strict_slashes=False)
route.add_url_rule(rule='/profil/delete/<id>', view_func=profil.delete, methods=['DELETE'], strict_slashes=False)
route.add_url_rule(rule='/profil/users/desable', view_func=profil.deactivated, methods=['GET'], strict_slashes=False)
route.add_url_rule(rule='/profil/update', view_func=profil.update, methods=['PUT'], strict_slashes=False)


route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)
route.add_url_rule(rule='', view_func=, methods=[], strict_slashes=False)