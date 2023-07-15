from flask import Flask, render_template, request, redirect, url_for
import json
from utils import load
from char import Char, Skill, Spell

app = Flask(__name__)

# Route for authentication
@app.route('/', methods=['POST', 'GET'])
def load_char():
    if request.method == 'POST':
        # Retrieve entered player name from the request
        entered_char_name = request.form['char_name']

        # Load the player information
        try:
            char = Char(entered_char_name, {}, {}, {}, {}, {})
            char.load()
            return redirect(url_for('charsheet', char_name=char.name))
        except:
            return redirect(url_for('create_char'))
        
    else:
        return render_template('login.html')

# Route for char creation
@app.route('/create', methods=['POST', 'GET'])
def create_char():
    # Retrieve form data
    if request.method == 'POST':
        char_name = request.form['char_name']
        skill1 = Skill(request.form['skill1_name'], request.form['skill1_effect'], request.form['skill1_damage'])
        skill1.save()
        skills = {
            request.form['skill1_name'] : skill1
        }
        spell1 = Spell(request.form['spell1_name'], request.form['spell1_effect'], request.form['spell1_damage'])
        spell1.save()
        spells = {
            request.form['spell1_name'] : spell1
        }
        stats = {
            'dex' : request.form['dex'],
            'int' : request.form['int'],
            'str' : request.form['str'],
            'wil' : request.form['wil'],
            'wis' : request.form['wis'],
            'cha' : request.form['cha']
        }

        # Create a new player object
        char = Char(char_name, skills=skills, spells=spells, stats=stats, items={}, gear={})
        char.save()

        return redirect(url_for('load_char'))

    else:
        return render_template('create_char.html')

# Route for the char page
@app.route('/charsheet/<char_name>')
def charsheet(char_name):
    char_info = load('data/chars.json', char_name)
    return render_template('charsheet.html', char_name=char_info['name'], gold=char_info['gold'], hp=char_info['hp'], items=char_info['items'], skills=char_info['skills'], stats=char_info['stats'], gear=char_info['gear'], spells=char_info['spells'])

if __name__ == '__main__':
    app.run()
