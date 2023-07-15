import unittest, json

from char import Char, Gear, Item, Skill, Spell


class TestChar(unittest.TestCase):
    def test_create_char(self):
        """
        Test that a new character is created correctly
        """
        skill = Skill('Skill1', None, None)
        char = Char('Test', {'Skill1' : skill}, {'Spell1' : None}, {'Stat1' : 'Value1'}, {'Item1' : None}, {'Gear1' : None})
        self.assertEqual(char.name, 'Test')
        self.assertEqual(char.gold, 0)
        self.assertEqual(char.items, {'Item1' : None})
        self.assertEqual(char.gear, {'Gear1' : None})
        self.assertEqual(char.skills, {'Skill1' : skill})
        self.assertEqual(char.spells, {'Spell1' : None})
        self.assertEqual(char.stats, {'Stat1' : 'Value1'})
    
    def test_create_char_empty(self):
        """
        Test that a new character is created correctly
        """
        char = Char('Test', {}, {}, {}, {}, {})
        self.assertEqual(char.name, 'Test')
        self.assertEqual(char.gold, 0)
        self.assertEqual(char.items, {})
        self.assertEqual(char.gear, {})
        self.assertEqual(char.skills, {})
        self.assertEqual(char.stats, {})
    
    def test_save_char(self):
        """
        Test that a character is saved correctly
        """
        char = Char('Test', {'Skill1' : Skill('Skill1', None, None)}, {'Spell1' : None}, {'Stat1' : 'Value1'}, {'Item1' : None}, {'Gear1' : None})
        char.save()
        with open(f'data/chars.json', 'r') as f:
            char_info = json.load(f)
        
        for info in char_info:
            if info['name'] == 'Test':
                char_info = info

        self.assertEqual(char_info['name'], 'Test')
        self.assertEqual(char_info['gold'], 0)
        self.assertEqual(char_info['items'], ['Item1'])
        self.assertEqual(char_info['gear'], ['Gear1'])
        self.assertEqual(char_info['skills'], ['Skill1'])
        self.assertEqual(char_info['spells'], ['Spell1'])
        self.assertEqual(char_info['stats'], {'Stat1' : 'Value1'})
    
    def test_save_char_empty(self):
        """
        Test that a character is saved correctly
        """
        char = Char('Test', {}, {}, {}, {}, {})
        char.save()
        with open(f'data/chars.json', 'r') as f:
            char_info = json.load(f)

        for info in char_info:
            if info['name'] == 'Test':
                char_info = info

        self.assertEqual(char_info['name'], 'Test')
        self.assertEqual(char_info['gold'], 0)
        self.assertEqual(char_info['items'], [])
        self.assertEqual(char_info['gear'], [])
        self.assertEqual(char_info['skills'], [])
        self.assertEqual(char_info['spells'], [])
        self.assertEqual(char_info['stats'], {})
    
    def test_load_char(self):
        """
        Test that a character is loaded correctly
        """
        skill = Skill('Skill1', None, None)
        skill.save()
        spell = Spell('Spell1', None, None)
        spell.save()
        item = Item('Item1', None, None)
        item.save()
        gear = Gear('Gear1', None, None)
        gear.save()
        char = Char('Test', {'Skill1' : skill}, {'Spell1' : spell}, {'Stat1' : 'Value1'}, {'Item1' : item}, {'Gear1' : gear})
        char.save()
        char.load()
        self.assertEqual(char.name, 'Test')
        self.assertEqual(char.gold, 0)
        self.assertEqual(list(char.items.keys()), ['Item1'])
        self.assertEqual(list(char.gear.keys()), ['Gear1'])
        self.assertEqual(list(char.skills.keys()), ['Skill1'])
        self.assertEqual(list(char.spells.keys()), ['Spell1'])
        self.assertEqual(char.stats, {'Stat1' : 'Value1'})
    
    def test_load_item(self):
        """
        Test that a item is loaded correctly
        """
        item = Item('Item1', 'Test', 0)
        item.save()
        item = Item('Item1', None, None)
        item.load()
        self.assertEqual(item.name, 'Item1')
        self.assertEqual(item.desc, 'Test')
        self.assertEqual(item.price, 0)
    
    def test_load_gear(self):
        """
        Test that a gear is loaded correctly
        """
        gear = Gear('Gear1', 'Test', {'Stat1' : 'Value1'})
        gear.save()
        gear = Gear('Gear1', None, None)
        gear.load()
        self.assertEqual(gear.name, 'Gear1')
        self.assertEqual(gear.desc, 'Test')
        self.assertEqual(gear.stats, {'Stat1' : 'Value1'})
    
    def test_save_item(self):
        """
        Test that a item is saved correctly
        """
        item = Item('Item1', 'Test', 0)
        item.save()
        with open(f'data/items.json', 'r') as f:
            item_info = json.load(f)
        
        for info in item_info:
            if info['name'] == 'Item1':
                item_info = info

        self.assertEqual(item_info['name'], 'Item1')
        self.assertEqual(item_info['desc'], 'Test')
        self.assertEqual(item_info['price'], 0)
    
    def test_save_gear(self):
        """
        Test that a gear is saved correctly
        """
        gear = Gear('Gear1', 'Test', {'Stat1' : 'Value1'})
        gear.save()
        with open(f'data/gear.json', 'r') as f:
            gear_info = json.load(f)
        
        for info in gear_info:
            if info['name'] == 'Gear1':
                gear_info = info

        self.assertEqual(gear_info['name'], 'Gear1')
        self.assertEqual(gear_info['desc'], 'Test')
        self.assertEqual(gear_info['stats'], {'Stat1' : 'Value1'})
    
    def test_change_balance(self):
        """
        Test that the balance is changed correctly
        """
        char = Char('Test', {}, {}, {}, {})
        char.change_balance(100)
        self.assertEqual(char.gold, 100)
        char.change_balance(-100)
        self.assertEqual(char.gold, 0)
        char.change_balance(-100)
        self.assertEqual(char.gold, 0)
        char.change_balance(100)
        self.assertEqual(char.gold, 100)
    
    def test_damage(self):
        """
        Test that the character is damaged correctly
        """
        char = Char('Test', {}, {}, {}, {})
        char.damage(10)
        self.assertEqual(char.hp, 10)
        char.damage(10)
        self.assertEqual(char.hp, 0)
        char.damage(10)
        self.assertEqual(char.hp, 0)
    
    def test_heal(self):
        """
        Test that the character is healed correctly
        """
        char = Char('Test', {}, {}, {}, {})
        char.damage(10)
        self.assertEqual(char.hp, 10)
        char.heal(10)
        self.assertEqual(char.hp, 20)
        char.heal(10)
        self.assertEqual(char.hp, 20)


if __name__ == '__main__':
    unittest.main()
