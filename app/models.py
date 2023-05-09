from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
db = SQLAlchemy()

class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), unique=True, nullable=False)
    challenge_rating = db.Column(db.String(400), unique=False, nullable=False)
    xp = db.Column(db.Integer, unique=False, nullable=False)
    size = db.Column(db.String(400), unique=False, nullable=False)
    type = db.Column(db.String(400), unique=False, nullable=False)
    languages = db.Column(db.String(400), unique=False, nullable=False)
    armor_class = db.Column(db.Integer, unique=False, nullable=False)
    armor_type = db.Column(db.String(400), unique=False, nullable=False)
    hit_points = db.Column(db.Integer, unique=False, nullable=False)
    damage_vulnerabilities = db.Column(db.String(3500), unique=False, nullable=False)
    damage_resistances = db.Column(db.String(3500), unique=False, nullable=False)
    damage_immunities = db.Column(db.String(3500), unique=False, nullable=False)
    condition_immunities = db.Column(db.String(3500), unique=False, nullable=False)
    darkvision = db.Column(db.String(400), unique=False, nullable=False)
    blindsight = db.Column(db.String(400), unique=False, nullable=False)
    tremorsense = db.Column(db.String(400), unique=False, nullable=False)
    truesight = db.Column(db.String(400), unique=False, nullable=False)
    passive_perception = db.Column(db.Integer, unique=False, nullable=False)
    walk_speed = db.Column(db.String(400), unique=False, nullable=False)
    climb_speed = db.Column(db.String(400), unique=False, nullable=False)
    fly_speed = db.Column(db.String(400), unique=False, nullable=False)
    swim_speed = db.Column(db.String(400), unique=False, nullable=False)
    burrow_speed = db.Column(db.String(400), unique=False, nullable=False)
    strength_modifier = db.Column(db.Integer, unique=False, nullable=False)
    dexterity_modifier = db.Column(db.Integer, unique=False, nullable=False)
    constitution_modifier = db.Column(db.Integer, unique=False, nullable=False)
    intelligence_modifier = db.Column(db.Integer, unique=False, nullable=False)
    wisdom_modifier = db.Column(db.Integer, unique=False, nullable=False)
    charisma_modifier = db.Column(db.Integer, unique=False, nullable=False)
    strength = db.Column(db.Integer, unique=False, nullable=False)
    dexterity = db.Column(db.Integer, unique=False, nullable=False)
    constitution = db.Column(db.Integer, unique=False, nullable=False)
    intelligence = db.Column(db.Integer, unique=False, nullable=False)
    wisdom = db.Column(db.Integer, unique=False, nullable=False)
    charisma = db.Column(db.Integer, unique=False, nullable=False)
    actions = db.Column(db.String(3500), unique=False, nullable=False)
    special_abilities = db.Column(db.String(3500), unique=False, nullable=False)
    legendary_actions = db.Column(db.String(3500), unique=False, nullable=False)
    image = db.Column(db.String(400), unique=False, nullable=False)

    def __init__(self, name, challenge_rating, xp, size, type, languages, armor_class, armor_type, hit_points, damage_vulnerabilities, damage_resistances, damage_immunities, darkvision, blindsight, tremorsense, truesight, passive_perception, walk_speed, climb_speed, fly_speed, swim_speed, burrow_speed, strength, dexterity, constitution, intelligence, wisdom, charisma, actions, special_abilities, legendary_actions, image, condition_immunities, strength_modifier, dexterity_modifier, constitution_modifier, intelligence_modifier, wisdom_modifier, charisma_modifier):
        self.name = name
        self.challenge_rating = challenge_rating
        self.xp = xp
        self.size = size
        self.type = type
        self.languages = languages
        self.armor_class = armor_class
        self.armor_type = armor_type
        self.hit_points = hit_points
        self.damage_vulnerabilities = damage_vulnerabilities
        self.damage_resistances = damage_resistances
        self.damage_immunities = damage_immunities
        self.condition_immunities = condition_immunities
        self.darkvision = darkvision
        self.blindsight = blindsight
        self.tremorsense = tremorsense
        self.truesight = truesight
        self.passive_perception = passive_perception
        self.walk_speed = walk_speed
        self.climb_speed = climb_speed
        self.fly_speed = fly_speed
        self.swim_speed = swim_speed
        self.burrow_speed = burrow_speed
        self.strength_modifier = strength_modifier
        self.dexterity_modifier = dexterity_modifier
        self.constitution_modifier = constitution_modifier
        self.intelligence_modifier = intelligence_modifier
        self.wisdom_modifier = wisdom_modifier
        self.charisma_modifier = charisma_modifier
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.actions = actions
        self.special_abilities = special_abilities
        self.legendary_actions = legendary_actions
        self.image = image

    def saveMonster(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "challenge_rating": self.challenge_rating,
            "xp": self.xp,
            "size": self.size,
            "type": self.type,
            "languages": self.languages,
            "armor_class": self.armor_class,
            "armor_type": self.armor_type,
            "hit_points": self.hit_points,
            "damage_vulnerabilities": self.damage_vulnerabilities,
            "damage_resistances": self.damage_resistances,
            "damage_immunities": self.damage_immunities,
            "condition_immunities": self.condition_immunities,
            "darkvision": self.darkvision,
            "blindsight": self.blindsight,
            "tremorsense": self.tremorsense,
            "truesight": self.truesight,
            "passive_perception": self.passive_perception,
            "walk_speed": self.walk_speed,
            "climb_speed": self.climb_speed,
            "fly_speed": self.fly_speed,
            "swim_speed": self.swim_speed,
            "burrow_speed": self.burrow_speed,
            "strength_modifier": self.strength_modifier,
            "dexterity_modifier": self.dexterity_modifier,
            "constitution_modifier": self.constitution_modifier,
            "intelligence_modifier": self.intelligence_modifier,
            "wisdom_modifier": self.wisdom_modifier,
            "charisma_modifier": self.charisma_modifier,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
            "actions": self.actions,
            "special_abilities": self.special_abilities,
            "legendary_actions": self.legendary_actions,
            "image": self.image
        }


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(400), unique=True, nullable=False)
    name = db.Column(db.String(400), unique=False, nullable=False)

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    def create(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
        }
    
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(400), unique=False, nullable=False)
    class_type = db.Column(db.String(400), unique=False, nullable=False)
    level = db.Column(db.Integer, unique=False, nullable=False)
    alignment = db.Column(db.String(400), unique=False, nullable=False)
    user_uid = db.Column(db.String, db.ForeignKey('user.uid'), nullable=False)

    def __init__(self, race, class_type, level, alignment, user_uid):
        self.race = race
        self.class_type = class_type
        self.level = level
        self.alignment = alignment
        self.user_uid = user_uid

    def create(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "race": self.race,
            "class_type": self.class_type,
            "level": self.level,
            "alignment": self.alignment,
        }


