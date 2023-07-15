import unittest, json

from utils import save, load

class TestUtil(unittest.TestCase):
    def test_save(self):
        """
        Test that a new entry is added to the JSON file
        """
        save('data/test.json', {'name' : 'Test1', 'desc' : 'Test1'})
        save('data/test.json', {'name' : 'Test2', 'desc' : 'Test2'})
        with open('data/test.json', 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [{'name' : 'Test1', 'desc' : 'Test1'}, {'name' : 'Test2', 'desc' : 'Test2'}])
    
    def test_load(self):
        """
        Test that an entry is retrieved from the JSON file
        """
        save('data/test.json', {'name' : 'Test1', 'desc' : 'Test1'})
        save('data/test.json', {'name' : 'Test2', 'desc' : 'Test2'})
        self.assertEqual(load('data/test.json', 'Test1'), {'name' : 'Test1', 'desc' : 'Test1'})
        self.assertEqual(load('data/test.json', 'Test2'), {'name' : 'Test2', 'desc' : 'Test2'})


if __name__ == '__main__':
    unittest.main()