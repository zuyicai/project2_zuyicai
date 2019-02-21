#to write some code to make your Flask app easier.
import pandas as pd
import random

movie_info_raw = pd.DataFrame(pd.read_csv('movies_clean.csv',header=0))# use pandas to read the clean data csv
movie_info = movie_info_raw.fillna(value="NA")#filling NA
info_nona = movie_info_raw['IMDB Rating'].fillna(value=0)#delete na in rating column in order to run recommend function


class Movie:
    length = len(movie_info['Title'])#Get the number of records in movies_clean.csv

    def __init__ (self,movie_info,i):#Movie that accepts as constructor input one row of the movies_clean.csv file
        self.title = movie_info["Title"][i]
        self.US_gross = movie_info['US Gross'][i]
        self.worldwide_gross = movie_info['Worldwide Gross'][i]
        self.US_DVD_Sales = movie_info['US DVD Sales'][i]
        self.production_budget = movie_info['Production Budget'][i]
        self.release_date = movie_info['Release Date'][i]
        self.MPAA_rating = movie_info['MPAA Rating'][i]
        self.running_time = movie_info['Running Time (min)'][i]
        self.distributor = movie_info['Distributor'][i]
        self.source = movie_info['Source'][i]
        self.major_genre = movie_info['Major Genre'][i]
        self.creative_type = movie_info['Creative Type'][i]
        self.director = movie_info['Director'][i]
        self.rotten_tomatoes_ratings = movie_info['Rotten Tomatoes Rating'][i]
        self.IMDB_rating = movie_info['IMDB Rating'][i]
        self.IMDB_votes = movie_info['IMDB Votes'][i]


    def ratings(self,amt):#To get movies and their ratings
        self.amt = amt
        title_list=[]
        i = 0
        while i < int(amt):
            rate = Movie(movie_info,random.randint(0,3134))
            title_list.append(rate.title+' | '+str(rate.IMDB_rating))
            i = i+1
        return title_list#return a list of movies. The length will depend on amt


    def recommend(self,amt):#To get highly recommended movies and their ratings
        self.amt = amt
        thelist=[]
        j = 0
        while j < int(amt):
            i = random.randint(0,self.length-1)
            highscore = Movie(movie_info,i)
            if int(info_nona[i])>=8:
                thelist.append(highscore.title+' | '+str(highscore.IMDB_rating))
                j = j+1
        return thelist#return a list of movies. The length will depend on amt

if __name__ == "__main__":
    pass
