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



# def anivault_list_fragment():
#     raw_json = read_file(os.path.join(app.root_path, 'data', 'anime_list.json'))
#     anime_list = json.loads(raw_json)    
#     return render_template('anivault/mytable.html', animes=anime_list)
@app.route('/anivault/list')
def anivault_list_fragment():
    url = "https://api.jikan.moe/v4/top/anime"

    try:
        response = urlopen(url)
        data_json = json.loads(response.read())

        if "data" not in data_json:
            return render_template('anivault/mytable.html', animes=[])

        anime_list = []

        for anime in data_json["data"]:
            anime_list.append({
                "title_english": anime.get("title_english") or anime.get("title"),
                "image_url": anime.get("images", {}).get("jpg", {}).get("image_url"),
                "year": anime.get("year"),
                "episodes": anime.get("episodes"),
                "synopsis": anime.get("synopsis"),
                "score": anime.get("score"),
                "genres": [g.get("name") for g in anime.get("genres", [])]
            })

        return render_template('anivault/mytable.html', animes=anime_list)

    except Exception:
        return render_template('anivault/mytable.html', animes=[])


def read_file(filename, mode="rt"):
    with open(filename, mode, encoding='utf-8') as fin:
        return fin.read()


