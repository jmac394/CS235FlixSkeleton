from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import adapters.repository as repo
import utilities.utilities as utilities
import news.services as services

from authentication.authentication import login_required


# Configure Blueprint.
news_blueprint = Blueprint(
    'news_bp', __name__)


@news_blueprint.route('/movies_by_date', methods=['GET'])
def movies_by_date():
    # Read query parameters.
    target_date = request.args.get('date')
    movie_to_show_comments = request.args.get('view_reviews_for')

    # Fetch the first and last articles in the series.
    first_movie = services.get_first_movie(repo.repo_instance)
    last_movie = services.get_last_movie(repo.repo_instance)

    if target_date is None:
        # No date query parameter, so return articles from day 1 of the series.
        target_date = first_movie['date']
    else:
        # Convert target_date from string to date.
        target_date = date.fromisoformat(target_date)

    if movie_to_show_comments is None:
        # No view-comments query parameter, so set to a non-existent article id.
        movie_to_show_comments = -1
    else:
        # Convert article_to_show_comments from string to int.
        movie_to_show_comments = int(moive_to_show_comments)

    # Fetch article(s) for the target date. This call also returns the previous and next dates for articles immediately
    # before and after the target date.
    movies, previous_date, next_date = services.get_movies_by_date(target_date, repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if len(movies) > 0:
        # There's at least one article for the target date.
        if previous_date is not None:
            # There are articles on a previous date, so generate URLs for the 'previous' and 'first' navigation buttons.
            prev_movie_url = url_for('news_bp.movies_by_date', date=previous_date.isoformat())
            first_movie_url = url_for('news_bp.movies_by_date', date=first_movie['date'].isoformat())

        # There are articles on a subsequent date, so generate URLs for the 'next' and 'last' navigation buttons.
        if next_date is not None:
            next_movie_url = url_for('news_bp.movies_by_date', date=next_date.isoformat())
            last_movie_url = url_for('news_bp.movies_by_date', date=last_mvoie['date'].isoformat())

        # Construct urls for viewing article comments and adding comments.
        for movie in movies:
            movie['view_review_url'] = url_for('news_bp.movies_by_date', date=target_date, view_reviews_for=movie['id'])
            movie['add_reviews_url'] = url_for('news_bp.review_on_movie', article=movie['id'])

        # Generate the webpage to display the articles.
        return render_template(
            'news/movies.html',
            title='Movies',
            movies_title=target_date.strftime('%A %B %e %Y'),
            movies=movies,
            selected_movies=utilities.get_selected_movies(len(movies) * 2),
            genre_urls=utilities.get_genres_and_urls(),
            actor_urls=utilities.get_actors_and_urls(),
            director_urls=utilities.get_directors_and_urls(),
            first_movie_url=first_movie_url,
            last_movie_url=last_movie_url,
            prev_movie_url=prev_movie_url,
            next_movie_url=next_movie_url,
            show_reviews_for_movie=movie_to_show_reviews
        )

    # No articles to show, so return the homepage.
    return redirect(url_for('home_bp.home'))


@news_blueprint.route('/movies_by_actor', methods=['GET'])
def movies_by_actor():
    movies_per_page = 3

    # Read query parameters.
    actor_name = request.args.get('actor')
    cursor = request.args.get('cursor')
    movie_to_show_reviews = request.args.get('view_reviews_for')

    if movie_to_show_reviews is None:
        # No view-comments query parameter, so set to a non-existent article id.
        movie_to_show_reviews = -1
    else:
        # Convert article_to_show_comments from string to int.
        movie_to_show_reviews = int(movie_to_show_reviews)

    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)

    # Retrieve article ids for articles that are tagged with tag_name.
    movie_ids = services.get_movie_ids_for_actor(actor_name, repo.repo_instance)

    # Retrieve the batch of articles to display on the Web page.
    movies = services.get_movies_by_id(movie_ids[cursor:cursor + movies_per_page], repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if cursor > 0:
        # There are preceding articles, so generate URLs for the 'previous' and 'first' navigation buttons.
        prev_movie_url = url_for('news_bp.movies_by_actor', actor=actor_name, cursor=cursor - movies_per_page)
        first_movie_url = url_for('news_bp.movies_by_actor', actor=actor_name)

    if cursor + movies_per_page < len(movie_ids):
        # There are further articles, so generate URLs for the 'next' and 'last' navigation buttons.
        next_movie_url = url_for('news_bp.movies_by_actor', actor=actor_name, cursor=cursor + movies_per_page)

        last_cursor = movies_per_page * int(len(movie_ids) / movies_per_page)
        if len(movie_ids) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('news_bp.movies_by_actor', actor=actor_name, cursor=last_cursor)

    # Construct urls for viewing article comments and adding comments.
    for movie in movies:
        movie['view_review_url'] = url_for('news_bp.movies_by_actor', actor=actor_name, cursor=cursor, view_reviews_for=movie['id'])
        movie['add_review_url'] = url_for('news_bp.review_on_movie', movie=movie['id'])

    # Generate the webpage to display the articles.
    return render_template(
        'news/movies.html',
        title='Movies',
        movies_title='Movies starring ' + actor_name,
        movies=movies,
        selected_movies=utilities.get_selected_movies(len(movies) * 2),
        actor_urls=utilities.get_actors_and_urls(),
        first_movie_url=first_movie_url,
        last_movie_url=last_movie_url,
        prev_movie_url=prev_movie_url,
        next_movie_url=next_movie_url,
        show_reviews_for_movie=movie_to_show_reviews
    )


@news_blueprint.route('/movies_by_director', methods=['GET'])
def movies_by_director():
    movies_per_page = 3

    # Read query parameters.
    director_name = request.args.get('director')
    cursor = request.args.get('cursor')
    movie_to_show_reviews = request.args.get('view_reviews_for')

    if movie_to_show_reviews is None:
        # No view-comments query parameter, so set to a non-existent article id.
        movie_to_show_reviews = -1
    else:
        # Convert article_to_show_comments from string to int.
        movie_to_show_reviews = int(movie_to_show_reviews)

    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)

    # Retrieve article ids for articles that are tagged with tag_name.
    movie_ids = services.get_movie_ids_for_director(director_name, repo.repo_instance)

    # Retrieve the batch of articles to display on the Web page.
    movies = services.get_movies_by_id(movie_ids[cursor:cursor + movies_per_page], repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if cursor > 0:
        # There are preceding articles, so generate URLs for the 'previous' and 'first' navigation buttons.
        prev_movie_url = url_for('news_bp.movies_by_director', director=director_name, cursor=cursor - movies_per_page)
        first_movie_url = url_for('news_bp.movies_by_director', director=director_name)

    if cursor + movies_per_page < len(movie_ids):
        # There are further articles, so generate URLs for the 'next' and 'last' navigation buttons.
        next_movie_url = url_for('news_bp.movies_by_director', actor=director_name, cursor=cursor + movies_per_page)

        last_cursor = movies_per_page * int(len(movie_ids) / movies_per_page)
        if len(movie_ids) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('news_bp.movies_by_director', director=director_name, cursor=last_cursor)

    # Construct urls for viewing article comments and adding comments.
    for movie in movies:
        movie['view_review_url'] = url_for('news_bp.movies_by_director', director=director_name, cursor=cursor, view_reviews_for=movie['id'])
        movie['add_review_url'] = url_for('news_bp.review_on_movie', movie=movie['id'])

    # Generate the webpage to display the articles.
    return render_template(
        'news/movies.html',
        title='Movies',
        movies_title='Movies directed by ' + director_name,
        movies=movies,
        selected_movies=utilities.get_selected_movies(len(movies) * 2),
        director_urls=utilities.get_directors_and_urls(),
        first_movie_url=first_movie_url,
        last_movie_url=last_movie_url,
        prev_movie_url=prev_movie_url,
        next_movie_url=next_movie_url,
        show_reviews_for_movie=movie_to_show_reviews
    )


@news_blueprint.route('/movies_by_genre', methods=['GET'])
def movies_by_genre():
    movies_per_page = 3

    # Read query parameters.
    genre_name = request.args.get('genre')
    cursor = request.args.get('cursor')
    movie_to_show_reviews = request.args.get('view_reviews_for')

    if movie_to_show_reviews is None:
        # No view-comments query parameter, so set to a non-existent article id.
        movie_to_show_reviews = -1
    else:
        # Convert article_to_show_comments from string to int.
        movie_to_show_reviews = int(movie_to_show_reviews)

    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)

    # Retrieve article ids for articles that are tagged with tag_name.
    movie_ids = services.get_movie_ids_for_genre(genre_name, repo.repo_instance)

    # Retrieve the batch of articles to display on the Web page.
    movies = services.get_movies_by_id(movie_ids[cursor:cursor + movies_per_page], repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if cursor > 0:
        # There are preceding articles, so generate URLs for the 'previous' and 'first' navigation buttons.
        prev_movie_url = url_for('news_bp.movies_by_genre', genre=genre_name, cursor=cursor - movies_per_page)
        first_movie_url = url_for('news_bp.movies_by_genre', genre=genre_name)

    if cursor + movies_per_page < len(movie_ids):
        # There are further articles, so generate URLs for the 'next' and 'last' navigation buttons.
        next_movie_url = url_for('news_bp.movies_by_genre', genre=genre_name, cursor=cursor + movies_per_page)

        last_cursor = movies_per_page * int(len(movie_ids) / movies_per_page)
        if len(movie_ids) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('news_bp.movies_by_genre', genre=genre_name, cursor=last_cursor)

    # Construct urls for viewing article comments and adding comments.
    for movie in movies:
        movie['view_review_url'] = url_for('news_bp.movies_by_genre', genre=genre_name, cursor=cursor, view_reviews_for=movie['id'])
        movie['add_review_url'] = url_for('news_bp.review_on_movie', movie=movie['id'])

    # Generate the webpage to display the articles.
    return render_template(
        'news/movies.html',
        title='Movies',
        movies_title= genre_name + " movies",
        movies=movies,
        selected_movies=utilities.get_selected_movies(len(movies) * 2),
        genre_urls=utilities.get_genres_and_urls(),
        first_movie_url=first_movie_url,
        last_movie_url=last_movie_url,
        prev_movie_url=prev_movie_url,
        next_movie_url=next_movie_url,
        show_reviews_for_movie=movie_to_show_reviews
    )


@news_blueprint.route('/review', methods=['GET', 'POST'])
@login_required
def review_on_article():
    # Obtain the username of the currently logged in user.
    username = session['username']

    # Create form. The form maintains state, e.g. when this method is called with a HTTP GET request and populates
    # the form with an article id, when subsequently called with a HTTP POST request, the article id remains in the
    # form.
    form = ReviewForm()

    if form.validate_on_submit():
        # Successful POST, i.e. the comment text has passed data validation.
        # Extract the article id, representing the commented article, from the form.
        movie_id = int(form.movie_id.data)

        # Use the service layer to store the new comment.
        services.add_review(movie_id, form.review.data, username, repo.repo_instance)

        # Retrieve the article in dict form.
        movie = services.get_movie(moive_id, repo.repo_instance)

        # Cause the web browser to display the page of all articles that have the same date as the commented article,
        # and display all comments, including the new comment.
        return redirect(url_for('news_bp.movies_by_date', date=movie['date'], view_reviews_for=movie_id))

    if request.method == 'GET':
        # Request is a HTTP GET to display the form.
        # Extract the article id, representing the article to comment, from a query parameter of the GET request.
        movie_id = int(request.args.get('movie'))

        # Store the article id in the form.
        form.movie_id.data = movie_id
    else:
        # Request is a HTTP POST where form validation has failed.
        # Extract the article id of the article being commented from the form.
        movie_id = int(form.movie_id.data)

    # For a GET or an unsuccessful POST, retrieve the article to comment in dict form, and return a Web page that allows
    # the user to enter a comment. The generated Web page includes a form object.
    movie = services.get_movie(movie_id, repo.repo_instance)
    return render_template(
        'news/review_on_movie.html',
        title='Edit movie',
        movie=movie,
        form=form,
        handler_url=url_for('news_bp.review_on_movie'),
        selected_movies=utilities.get_selected_movies(),
        actor_urls=utilities.get_actors_and_urls(),
        director_urls=utilities.get_directors_and_urls(),
        genre_urls=utilities.get_genres_and_urls()
    )


class ProfanityFree:
    def __init__(self, message=None):
        if not message:
            message = u'Field must not contain profanity'
        self.message = message

    def __call__(self, form, field):
        if profanity.contains_profanity(field.data):
            raise ValidationError(self.message)


class ReviewForm(FlaskForm):
    review = TextAreaField('Review', [
        DataRequired(),
        Length(min=4, message='Your review is too short'),
        ProfanityFree(message='Your review must not contain profanity')])
    movie_id = HiddenField("Movie id")
    submit = SubmitField('Submit')
