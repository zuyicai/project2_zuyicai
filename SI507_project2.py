#in the directory for the Flask app you'll write, and add import statements and comments to it to indicate structure/your plans/your goals for it.
from flask import Flask, render_template
from movies_tools import Movie,movie_info
# import statements

# Set up application
app = Flask(__name__)

# Routes
@app.route('/')#http://127.0.0.1:5000/
def home_page():
    nu_movie = Movie
    return '<h1> {} movies recorded</h1>'.format(nu_movie.length)
    #(results will depend upon how many movies are in your movies_clean.csv file…!)

@app.route('/movies/ratingsdirectly/<amt>/')#http://127.0.0.1:5000/movies/ratingsdirectly/5/
#This is the route to get ratings without the render_template
def movie_rating(amt):
    movierate = Movie(movie_info,int(amt))
    movie_list0 = movierate.ratings(int(amt))
    sample_movie = '<br>'.join(movie_list0)
    return '<h1> {} </h1>'.format(sample_movie)


@app.route('/movies/ratings/<amt>/')#http://127.0.0.1:5000/movies/ratings/10/
#This is the route to get ratings with the render_template
def movie_rating_template(amt):
    movie_sample = Movie(movie_info,int(amt))
    movie_list1 = movie_sample.ratings(int(amt))
    return render_template("movie_rating_template.html",movie_list=movie_list1)


@app.route('/movies/recommend/<amt>/')#http://127.0.0.1:5000/movies/recommend/20/
# This is the template version of highly recommended <amt> movies(all scored above 8)
def movie_highly_recommend(amt):
    recommended_movie = Movie(movie_info,int(amt))
    high_score_list = recommended_movie.recommend(int(amt))
    return render_template("high_score.html",movie_list=high_score_list)


if __name__ == '__main__':
    app.run()
