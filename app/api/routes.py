from flask import request, Blueprint
from ..models import User, Monster, Character
from flask_cors import cross_origin



api = Blueprint('api', __name__, url_prefix='/api')

@api.post('/users')
def create_user():
    uid = request.json.get('uid')
    name = request.json.get('displayName')

    user = User.query.filter_by(uid=uid).first()

    if user:
        return {'status': 'ok', 'message': 'Unable to create user. User already exists', 'user': user.to_dict()}
    user = User(uid=uid, name=name)
    user.create()
    return {'status': 'ok', 'user': user.to_dict()}

@api.get('/monsters')
def get_monsters():
    monsters = Monster.query.all()
    if not monsters:
        return {'status': 'not ok', 'message': 'Unable to get monsters'}
    return {'status': 'ok', 'monsters': [monster.to_dict() for monster in monsters]}

@api.get('/monsters/<int:monsterid>')
def get_monster(id):
    monster = Monster.query.get(id)
    if not monster:
        return {'status': 'not ok', 'message': 'Unable to get monster'}
    return {'status': 'ok', 'monster': monster.to_dict()}


@api.post('/character')
def create_character():
    print("i ran")
    user_uid = request.json.get('user_uid')
    userdata = request.json.get('userData')
    race = userdata["race"]
    class_type = userdata["class_type"]
    level = userdata["level"]
    alignment = userdata["alignment"]
    user = User.query.filter_by(uid=user_uid).first()
    print(user)
    if not user_uid or not user:
        return {'status': 'not ok', 'message': 'Unable to create character'}
    character = Character(race=race, class_type=class_type, level=level, alignment=alignment, user_uid=user_uid)
    character.create()
    return {'status': 'ok', 'character': character.to_dict()}


# @api.post('/tweets')
# def create_tweet():
#     user_uid = request.json.get('user_uid')
#     body = request.json.get('body')
#     user = User.query.filter_by(uid=user_uid).first()
#     if not body or not user_uid or not user:
#         return {'status': 'not ok', 'message': 'Unable to create tweet'}
#     tweet = Tweet(user_uid=user_uid, body=body).create()
#     return {'status': 'ok', 'tweet': tweet.to_dict()}



