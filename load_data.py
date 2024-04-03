import json

with open('s17.json') as user_file:
    file_contents = user_file.read()
data = json.loads(file_contents)

def encode(arr):
    i = 0
    return_dict = {}
    for item in arr:
        return_dict[item] = i
        i += 1
    return return_dict

tower_names = [
    # Primary
    'DartMonkey',
    'TackShooter',
    'BombShooter',
    'BoomerangMonkey',
    'GlueGunner',
    'IceMonkey',

    # Military
    'DartlingGunner',
    'MonkeySub',
    'SniperMonkey',
    'MonkeyAce',
    'MortarMonkey',
    'HeliPilot',
    'MonkeyBuccaneer',

    # Magic
    'WizardMonkey',
    'Alchemist',
    'Druid',
    'SuperMonkey',
    'NinjaMonkey',

    # Support
    'SpikeFactory',
    'MonkeyVillage',
    'BananaFarm',
    'EngineerMonkey'
]

hero_names = [
    'Quincy',
    'Gwendolin',
    'Obyn_Ocean',
    'Quincy_Cyber',
    'Obyn',
    'StrikerJones',
    'Gwendolin_Science',
    'StrikerJones_Biker',
    'Churchill',
    'Churchill_Sentai',
    'Benjamin',
    'Benjamin_DJ',
    'Ezili',
    'Ezili_SmudgeCat',
    'PatFusty',
    'PatFusty_Snowman',
    'Jericho',
    'Jericho_Highwayman',
    'Jericho_StarCaptain',
    'Adora'
]

map_names = [
    'banana_depot_scene',
    'basalt_columns',
    'building_site_scene',
    'bloon_bot_factory',
    'basalt_colums',
    'castle_ruins',
    'cobra_command',
    'dino_graveyard',
    'garden',
    'glade',
    'inflection',
    'koru',
    'oasis',
    'ports',
    'sands_of_time',
    'star',
    'pirate_cove',
    'precious_space',
    'sun_palace',
    'off_tide',
    'salmon_pool'
]

tower_encoding = encode(tower_names)
hero_encoding = encode(hero_names)
map_encoding = encode(map_names)

# Removes matches that didn't occur in HOM-pool maps
i = 0
while i < len(data):
    if data[i]['body']['map'] not in map_names:
        data.pop(i)
    else:
        i += 1