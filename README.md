# Project2_zuyicai: A movie recommendation app and the database plan

This's a whole web application — a very simple one, using the web framework called Flask. Using this small application, you can get different outputs in the form of URLs.

movies_tools.py is the file that I create the class and define the functional structure of this movie system; SI507_project2.py is the file that I put the movie system into practice with the appearance of URLs.

In addition, part 1 of this project is just code and a Flask app, including movies_tools.py, SI507_project2.py, requirement.txt, movies_clean.csv. Part 2 of this project is a plan(see SI507_movies_database_plan.jpeg) for creating a database to represent some of the data in movies_clean.csv file. I may build for an application or analysis later on.

My database diagram plan shows a viewer what tables should exist ( 4 tables: Movie, Director, Ratings, Distributor) and shows the fields each table contain. And I also show the primary key for each table and the relationships(many to many OR one to many). Hope it be clear enough to understand.

The follwing is the steps for running part 1:
Actually, I import Movie class and movie_info(a cleaned movie data csv) from movies_tools.py to make the use of "Movie" class and the cleaned data. Readers need to follow the steps to install everything needed to run this application.


## Getting Started

* Anaconda installed
* Open your terminal window! `cd` to the place where you want this project to go.
* This repository cloned to somewhere in your computer (the place).
```
git clone <git url>
```
* `cd` into where the project lives
* Create a virtual environment for it
```
virtualenv env
```
* Activate the virtual environment
```
$ source <projectname>-env/bin/activate    # For Mac/Linux...
$ source <projectname>-env/Scripts/activate    # For Windows
(project1-env) $     # you've succeeded if you see this after!
```
* install all requirement
```
pip install -r requirements.txt
```
```
Deactivate
```
* Just run the banking app!
```
python SI507_project2.py runserver
```
* Check out what’s happening in your terminal window!
* Open a web browser, type in and check out this URL:
http://127.0.0.1:5000/
* you will see "number movies recorded". Here number will depend upon how many movies are in your movies_clean.csv file
* ![Alt text](https://github.com/zuyicai/image/blob/master/h2.png)

* Open another tab and go to:
http://127.0.0.1:5000/movies/ratingsdirectly/10/
* e.g. http://127.0.0.1:5000/movies/ratingsdirectly/5/ you will see the following two images. One is for the 5 movies selected for you and the other one will be the 10 movies selected for you. (Here the amount of movies will depend on what you input in the URL:<amt>)
* ![Alt text](https://github.com/zuyicai/image/blob/master/10directly2.png)
* ![Alt text](https://github.com/zuyicai/image/blob/master/5directly2.png)
* This route is wrote without the use of "render_template". I just show this as a reference. It's not new knowledge in class these days but I want to remain it here.

* Now try going to:
http://127.0.0.1:5000/movies/ratings/10/
* e.g. http://127.0.0.1:5000/movies/ratings/5/ you will see the following two images. One is for the 5 movies selected for you and the other one will be the 10 movies selected for you. (Here the amount of movies will depend on what you input in the URL:<amt>)
* ![Alt text](https://github.com/zuyicai/image/blob/master/10rate2.png)
* ![Alt text](https://github.com/zuyicai/image/blob/master/5rate2.png)
* This route is wrote with the use of "render_template". It's what we learned recently in class. And this one has to do with the html file in templates file.

* Now try going to:
http://127.0.0.1:5000/movies/recommend/20/
* e.g. http://127.0.0.1:5000/movies/recommend/5/ you will see the following two images. One is for the 5 movies selected for you and the other one will be the 10 movies selected for you. What the difference here is that these movies are highly recommended for you because they are all scored above 8. They are totally deserve watching! Enjoy yourself~ :)(Here the amount of movies will depend on what you input in the URL:<amt>)
* ![Alt text](https://github.com/zuyicai/image/blob/master/10recom2.png)
* ![Alt text](https://github.com/zuyicai/image/blob/master/5recom2.png)

* Exit it / stop it running on the local server by typing `Control + C`
