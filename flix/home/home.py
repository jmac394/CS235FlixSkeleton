from flask import Blueprint, render_template

import covid.utilities.utilities as utilities


home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html',
        selected_movie=utilities.get_selected_movie(),
        actor_urls=utilities.get_actor_and_urls(),
        director_urls=utilities.get_director_and_urls(),
        genre_urls=utilities.get_genre_and_urls()
    )