__author__ = 'jhoelzer'

from flask import Flask, render_template
from tinydb import TinyDB
import random


app = Flask(__name__)
db = TinyDB('db.json')


@app.route('/')
def index():
    recipe = db.all()
    random_recipe = random.choice(recipe)
    print(random_recipe)
    return render_template('random_recipe.html', random_recipe=random_recipe)
