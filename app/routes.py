from app.models import db, Monster, User, Character, XpThreshholds
from flask import render_template, redirect, url_for
from app import app
import requests, json
from app.helpers import getName


# THIS IS ONLY TO ADD YOUR YOUR DB!!!!
# ADD THIS TO YOUR INDEX.HTML:
# <a href="{{ url_for('sendIt') }}" class="btn btn-dark">Add to Cart!</a>

# @app.route('/')
# def Home():
#     return redirect(url_for('productDB'))


# @app.route('/sendit') 
# def sendit():
#     for i in range(0, 334):
#         name = getName(i)
#         url = f'https://www.dnd5eapi.co/api/monsters/{name}'
#         response = requests.get(url)
#         if response.ok:
#             api = response.json()
#             print(api)
#             monster_info = {}
#             monster_info['name'] = api['name']
#             monster_info['challenge_rating'] = api['challenge_rating']
#             monster_info['xp'] = api['xp']
#             monster_info['size'] = api['size']
#             monster_info['type'] = api['type']
#             monster_info['languages'] = api['languages']

#             name = api['name'].lower()
#             name = name.replace(" ", "-")  # Replace spaces with hyphens
#             name = name.replace("'", "")  # Remove apostrophes
#             name = name.replace(",", "-")  # Replace commas with hyphens
#             name = name.replace("form", "")  # Remove the word "form"
#             monster_info['image'] = "https://www.dnd5eapi.co/api/images/monsters/" + name + ".png"


#             monster_info['armor_class'] = api['armor_class'][0]['value']
#             monster_info['armor_type'] = api['armor_class'][0]['type']
#             monster_info['hit_points'] = api['hit_points']

#             if api['damage_vulnerabilities'] == None:
#                 monster_info['damage_vulnerabilities'] = "None"
#             else:
#                 monster_info['damage_vulnerabilities'] = api['damage_vulnerabilities']
#             if api['damage_resistances'] == None:
#                 monster_info['damage_resistances'] = "None"
#             else:
#                 monster_info['damage_resistances'] = api['damage_resistances']
#             if api['damage_immunities'] == None:
#                 monster_info['damage_immunities'] = "None"
#             else:
#                 monster_info['damage_immunities'] = api['damage_immunities']

#             if api['condition_immunities'] == None:
#                 monster_info['condition_immunities'] = "None"
#             else:
#                 monster_info['condition_immunities'] = api['condition_immunities']
                
#             if 'darkvision' in api['senses']:
#                 monster_info['darkvision'] = api['senses']['darkvision']
#             else:
#                 monster_info['darkvision'] = '0'
#             if 'blindsight' in api['senses']:
#                 monster_info['blindsight'] = api['senses']['blindsight']
#             else:
#                 monster_info['blindsight'] = '0'
#             if 'tremorsense' in api['senses']:
#                 monster_info['tremorsense'] = api['senses']['tremorsense']
#             else:
#                 monster_info['tremorsense'] = '0'
#             if 'truesight' in api['senses']:
#                 monster_info['truesight'] = api['senses']['truesight']
#             else:
#                 monster_info['truesight'] = '0'
#             if 'passive_perception' in api['senses']:
#                 monster_info['passive_perception'] = api['senses']['passive_perception']
#             else:
#                 monster_info['passive_perception'] = '0'

#             if 'walk' in api['speed']:
#                 monster_info['walk_speed'] = api['speed']['walk']
#             else:
#                 monster_info['walk_speed'] = '0'
#             if 'climb' in api['speed']:
#                 monster_info['climb_speed'] = api['speed']['climb']
#             else:
#                 monster_info['climb_speed'] = '0'
#             if 'fly' in api['speed']:
#                 monster_info['fly_speed'] = api['speed']['fly']
#             else:
#                 monster_info['fly_speed'] = '0'
#             if 'swim' in api['speed']:
#                 monster_info['swim_speed'] = api['speed']['swim']
#             else:
#                 monster_info['swim_speed'] = '0'
#             if 'burrow' in api['speed']:
#                 monster_info['burrow_speed'] = api['speed']['burrow']
#             else:
#                 monster_info['burrow_speed'] = '0'

#             monster_info['strength_modifier'] = api['strength']/2 - 5
#             monster_info['dexterity_modifier'] = api['dexterity']/2 - 5
#             monster_info['constitution_modifier'] = api['constitution']/2 - 5
#             monster_info['intelligence_modifier'] = api['intelligence']/2 - 5
#             monster_info['wisdom_modifier'] = api['wisdom']/2 - 5
#             monster_info['charisma_modifier'] = api['charisma']/2 - 5
#             monster_info['strength'] = api['strength']
#             monster_info['dexterity'] = api['dexterity']
#             monster_info['constitution'] = api['constitution']
#             monster_info['intelligence'] = api['intelligence']
#             monster_info['wisdom'] = api['wisdom']
#             monster_info['charisma'] = api['charisma']

#             if api['actions'] == []:
#                 monster_info['actions'] = "None"
#             else:
#                 monster_info['actions'] = [[None, None], [None, None], [None, None], [None, None], [None, None]]
#                 monster_info['actions'][0][0] = api['actions'][0]['name']
#                 monster_info['actions'][0][1] = api['actions'][0]['desc']
#                 if len(api['actions']) > 1:
#                     monster_info['actions'][1][0] = api['actions'][1]['name']
#                     monster_info['actions'][1][1] = api['actions'][1]['desc']
#                 if len(api['actions']) > 2:
#                     monster_info['actions'][2][0] = api['actions'][2]['name']
#                     monster_info['actions'][2][1] = api['actions'][2]['desc']
#                 if len(api['actions']) > 3:
#                     monster_info['actions'][3][0] = api['actions'][3]['name']
#                     monster_info['actions'][3][1] = api['actions'][3]['desc']
#                 if len(api['actions']) > 4:
#                     monster_info['actions'][4][0] = api['actions'][4]['name']
#                     monster_info['actions'][4][1] = api['actions'][4]['desc']

#             if api['special_abilities'] == []:
#                 monster_info['special_abilities'] = "None"
#             else:
#                 monster_info['special_abilities'] = [[None, None], [None, None], [None, None], [None, None], [None, None]]
#                 monster_info['special_abilities'][0][0] = api['special_abilities'][0]['name']
#                 monster_info['special_abilities'][0][1] = api['special_abilities'][0]['desc']
#                 if len(api['special_abilities']) > 1:
#                     monster_info['special_abilities'][1][0] = api['special_abilities'][1]['name']
#                     monster_info['special_abilities'][1][1] = api['special_abilities'][1]['desc']
#                 if len(api['special_abilities']) > 2:
#                     monster_info['special_abilities'][2][0] = api['special_abilities'][2]['name']
#                     monster_info['special_abilities'][2][1] = api['special_abilities'][2]['desc']
#                 if len(api['special_abilities']) > 3:
#                     monster_info['special_abilities'][3][0] = api['special_abilities'][3]['name']
#                     monster_info['special_abilities'][3][1] = api['special_abilities'][3]['desc']
#                 if len(api['special_abilities']) > 4:
#                     monster_info['special_abilities'][4][0] = api['special_abilities'][4]['name']
#                     monster_info['special_abilities'][4][1] = api['special_abilities'][4]['desc']

#             if api['legendary_actions'] == []:
#                 monster_info['legendary_actions'] = "None"
#             else:
#                 monster_info['legendary_actions'] = [[None, None], [None, None], [None, None], [None, None], [None, None]]
#                 monster_info['legendary_actions'][0][0] = api['legendary_actions'][0]['name']
#                 monster_info['legendary_actions'][0][1] = api['legendary_actions'][0]['desc']
#                 if len(api['legendary_actions']) > 1:
#                     monster_info['legendary_actions'][1][0] = api['legendary_actions'][1]['name']
#                     monster_info['legendary_actions'][1][1] = api['legendary_actions'][1]['desc']
#                 if len(api['legendary_actions']) > 2:
#                     monster_info['legendary_actions'][2][0] = api['legendary_actions'][2]['name']
#                     monster_info['legendary_actions'][2][1] = api['legendary_actions'][2]['desc']
#                 if len(api['legendary_actions']) > 3:
#                     monster_info['legendary_actions'][3][0] = api['legendary_actions'][3]['name']
#                     monster_info['legendary_actions'][3][1] = api['legendary_actions'][3]['desc']
#                 if len(api['legendary_actions']) > 4:
#                     monster_info['legendary_actions'][4][0] = api['legendary_actions'][4]['name']
#                     monster_info['legendary_actions'][4][1] = api['legendary_actions'][4]['desc']

#             m = Monster(name = monster_info['name'], challenge_rating = monster_info['challenge_rating'], xp = monster_info['xp'], size = monster_info['size'], type = monster_info['type'], languages = monster_info['languages'], image = monster_info['image'], armor_class = monster_info['armor_class'], armor_type = monster_info['armor_type'], hit_points = monster_info['hit_points'], damage_vulnerabilities= monster_info['damage_vulnerabilities'], damage_resistances = monster_info['damage_resistances'], damage_immunities = monster_info['damage_immunities'], condition_immunities = monster_info['condition_immunities'], darkvision= monster_info['darkvision'], blindsight= monster_info['blindsight'], tremorsense= monster_info['tremorsense'], truesight= monster_info['truesight'], passive_perception= monster_info['passive_perception'], walk_speed= monster_info['walk_speed'], burrow_speed= monster_info['burrow_speed'], climb_speed= monster_info['climb_speed'], fly_speed= monster_info['fly_speed'], swim_speed= monster_info['swim_speed'], strength= monster_info['strength'], dexterity= monster_info['dexterity'], constitution= monster_info['constitution'], intelligence= monster_info['intelligence'], wisdom= monster_info['wisdom'], charisma= monster_info['charisma'], actions= monster_info['actions'], special_abilities= monster_info['special_abilities'], legendary_actions= monster_info['legendary_actions'], 
#                         strength_modifier= monster_info['strength_modifier'], dexterity_modifier= monster_info['dexterity_modifier'], constitution_modifier= monster_info['constitution_modifier'], intelligence_modifier= monster_info['intelligence_modifier'], wisdom_modifier= monster_info['wisdom_modifier'], charisma_modifier= monster_info['charisma_modifier'])
#             m.saveMonster()
#             print(f"{monster_info['name']} saved to database")
#     return render_template('index.html')

# @app.route('/xp')
# def xp():
#     xp_data = [
#         {"level": 1, "easy": 25, "medium": 50, "hard": 75, "deadly": 100},
#         {"level": 2, "easy": 50, "medium": 100, "hard": 150, "deadly": 200},
#         {"level": 3, "easy": 75, "medium": 150, "hard": 225, "deadly": 400},
#         {"level": 4, "easy": 125, "medium": 250, "hard": 375, "deadly": 500},
#         {"level": 5, "easy": 250, "medium": 500, "hard": 750, "deadly": 1100},
#         {"level": 6, "easy": 300, "medium": 600, "hard": 900, "deadly": 1400},
#         {"level": 7, "easy": 350, "medium": 750, "hard": 1100, "deadly": 1700},
#         {"level": 8, "easy": 450, "medium": 900, "hard": 1400, "deadly": 2100},
#         {"level": 9, "easy": 550, "medium": 1100, "hard": 1600, "deadly": 2400},
#         {"level": 10, "easy": 600, "medium": 1200, "hard": 1900, "deadly": 2800},
#         {"level": 11, "easy": 800, "medium": 1600, "hard": 2400, "deadly": 3600},
#         {"level": 12, "easy": 1000, "medium": 2000, "hard": 3000, "deadly": 4500},
#         {"level": 13, "easy": 1100, "medium": 2200, "hard": 3400, "deadly": 5100},
#         {"level": 14, "easy": 1250, "medium": 2500, "hard": 3800, "deadly": 5700},
#         {"level": 15, "easy": 1400, "medium": 2800, "hard": 4300, "deadly": 6400},
#         {"level": 16, "easy": 1600, "medium": 3200, "hard": 4800, "deadly": 7200},
#         {"level": 17, "easy": 2000, "medium": 3900, "hard": 5900, "deadly": 8800},
#         {"level": 18, "easy": 2100, "medium": 4200, "hard": 6300, "deadly": 9500},
#         {"level": 19, "easy": 2400, "medium": 4900, "hard": 7300, "deadly": 10900},
#         {"level": 20, "easy": 2800, "medium": 5700, "hard": 8500, "deadly": 12700}
#     ]
#     for xp_entry in xp_data:
#         xp = XpThreshholds(
#             level=xp_entry['level'],
#             easy=xp_entry['easy'],
#             medium=xp_entry['medium'],
#             hard=xp_entry['hard'],
#             deadly=xp_entry['deadly']
#         )
#         xp.saveXP()
#         print(f"XP for level {xp_entry['level']} saved to the database")


    
@app.route('/monsters')
def monsters():
    y = Monster.query.all()
    prodlist = [p.to_dict() for p in y]
    return {
        'status': 'ok',
        'data': prodlist,
        'item_count': len(prodlist)
    }

@app.route('/characters')
def characters():
    characters = Character.query.all()
    character_list = [character.to_dict() for character in characters]
    return {
        'status': 'ok',
        'data': character_list,
        'item_count': len(character_list)
    }

@app.route('/xpthreshholds')
def xpthreshholds():
    xp = XpThreshholds.query.all()
    xp_list = [x.to_dict() for x in xp]
    return {
        'status': 'ok',
        'data': xp_list,
        'item_count': len(xp_list)
    }

@app.route('/monsters/<int:monster_id>')
def monster(monster_id):
    product = Monster.query.filter(Monster.id == monster_id).first()
    if product:
        p = product.to_dict() # Assuming to_dict() method returns a dictionary with product data
        return ({
            'status': 'ok',
            'data': p,
            'item_count': 1 # Since you are returning a single product
        })
    else:
        return ({
            'status': 'error',
            'message': 'Product not found'
        }), 404 # Return a 404 status code if product not found
    