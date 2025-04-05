#!usr/bin/env python3

from flask import request, jsonify, redirect, url_for

from flask_login import current_user
from api.v1.views import api_v1
import json

promos = ['QQQ100']

@api_v1.route('/subs', methods=['POST'], strict_slashes=False)
def check_promo():
    """Check if a promo code is valid"""
    from app.models.user import User
    promo_code = request.json.get('promo')
    user = User.query.filter_by(id=current_user.id).first()


    if promo_code in promos:
        if user.role != 'student':
            return jsonify({'msg': "You already in this Plan."}), 400
        user.role = 'pro-student'
        user.save()
        return jsonify({"msg": "Subscription successful!"}), 200
    return jsonify({"error": "Unvalid promocode"}), 400
