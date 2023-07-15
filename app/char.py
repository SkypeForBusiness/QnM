import json
from utils import save, load

class Char():
    def __init__(self, name : str, skills : dict, spells : dict, stats : dict, items : dict = {}, gear : dict = {}):
        self.name = name
        self.gold = 0
        self.hp = 20
        self.items = items
        self.gear = gear
        self.skills = skills
        self.spells = spells
        self.stats = stats

    def save(self):
        char_info = {
            'name' : self.name,
            'gold' : self.gold,
            'hp' : self.hp,
            'items' : list(self.items.keys()),
            'gear' : list(self.gear.keys()),
            'skills' : list(self.skills.keys()),
            'spells' : list(self.spells.keys()),
            'stats' : self.stats
        }
        
        save(path='data/chars.json', data=char_info)
    
    def load(self):
        char_info = load(path='data/chars.json', name=self.name)
        if char_info is None:
            raise('Character not found')
        
        self.name = char_info['name']
        self.gold = char_info['gold']
        self.hp = char_info['hp']
        self.items = {item : Item(item, None, None).load() for item in char_info['items']}
        self.gear = {gear : Gear(gear, None, None).load() for gear in char_info['gear']}
        self.skills = {skill : Skill(skill, None, None).load() for skill in char_info['skills']}
        self.spells = {spell : Spell(spell, None, None).load() for spell in char_info['spells']}
        self.stats = char_info['stats']
    
    def add_item(self, item):
        self.items[item.name] = item
    
    def remove_item(self, item):
        del self.items[item.name]
    
    def add_gear(self, gear):
        self.gear[gear.name] = gear
    
    def remove_gear(self, gear):
        del self.gear[gear.name]
    
    def change_balance(self, amount):
        self.gold += amount
        if self.gold < 0:
            self.gold = 0
    
    def damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
    
    def heal(self, amount):
        self.hp += amount
        if self.hp > 20:
            self.hp = 20


class Gear():
    def __init__(self, name : str, desc : str, stats : dict):
        self.name = name
        self.desc = desc
        self.stats = stats
    
    def save(self):
        gear_info = {
            'name' : self.name,
            'desc' : self.desc,
            'stats' : self.stats
        }

        save(path='data/gear.json', data=gear_info)
    
    def load(self):
        gear_info = load(path='data/gear.json', name=self.name)
        self.name = gear_info['name']
        self.desc = gear_info['desc']
        self.stats = gear_info['stats']
        
        return self
        
class Item():
    def __init__(self, name : str, desc : str, price : int):
        self.name = name
        self.desc = desc
        self.price = price

    def save(self):
        item_info = {
            'name' : self.name,
            'desc' : self.desc,
            'price' : self.price
        }

        save(path='data/items.json', data=item_info)
    
    def load(self):
        item_info = load(path='data/items.json', name=self.name)
        self.name = item_info['name']
        self.desc = item_info['desc']
        self.price = item_info['price']

        return self

class Skill():
    def __init__(self, name : str, effect : str, damage : int):
        self.name = name
        self.effect = effect
        self.damage = damage
    
    def save(self):
        skill_info = {
            'name' : self.name,
            'effect' : self.effect,
            'damage' : self.damage
        }

        save(path='data/skills.json', data=skill_info)
    
    def load(self):
        skill_info = load(path='data/skills.json', name=self.name)
        self.name = skill_info['name']
        self.effect = skill_info['effect']
        self.damage = skill_info['damage']

        return self
    
class Spell():
    def __init__(self, name : str, effect : str, damage : int):
        self.name = name
        self.effect = effect
        self.damage = damage
    
    def save(self):
        spell_info = {
            'name' : self.name,
            'effect' : self.effect,
            'damage' : self.damage
        }

        save(path='data/spells.json', data=spell_info)
    
    def load(self):
        spell_info = load(path='data/spells.json', name=self.name)
        self.name = spell_info['name']
        self.effect = spell_info['effect']
        self.damage = spell_info['damage']

        return self