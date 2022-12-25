from typing import NoReturn

import jwt
import msgspec
from flask import abort, jsonify

from .database import User, db


class AuthMedium:
    def form(self, user_id: str, password: str) -> str:
        return jwt.encode(
            {'type': 0, 'bot_token': False},
            password,
            headers={'user_id': user_id},
            json_encoder=msgspec.json.encode,
        )

    def _abort(self) -> NoReturn:
        abort(jsonify({'_errors': ['Invalid Authentication']}))

    def verify(self, token: str) -> User:
        headers = jwt.get_unverified_header(token)

        try:
            user_id = int(headers['user_id'])
        except (KeyError, ValueError):
            self._abort()

        user_id = str(user_id)

        doc = db.users.find_one({'_id': user_id})

        if doc is None:
            self._abort()

        password = doc['password']

        try:
            jwt.decode(token, password)
        except jwt.DecodeError:
            self._abort()

        return True


auth = AuthMedium()