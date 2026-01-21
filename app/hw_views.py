# first_name 
# (nickname)
# student_id
# sec00x

import json
from urllib.request import urlopen
from urllib.parse import quote
from flask import (jsonify, render_template, request)
from app import app
import os

DEBUG = False

@app.route('/anivault')
def anivault_mylist():
    return render_template('anivault/index.html', active_tab='search')


@app.route('/anivault/list')
def anivault_list_fragment():
    raw_json = read_file(os.path.join(app.root_path, 'data', 'anime_list.json'))
    anime_list = json.loads(raw_json)    
    return render_template('anivault/mytable.html', animes=anime_list)


def read_file(filename, mode="rt"):
    with open(filename, mode, encoding='utf-8') as fin:
        return fin.read()


