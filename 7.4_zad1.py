import random
from operator import attrgetter

library = []

class Movie:
    def __init__(self, tittle, publ_year, genre, views_number):
        self.tittle = tittle
        self.publ_year = publ_year
        self.genre = genre
        self.views_number = views_number
    
    def __str__(self):
        return f'{self.tittle} ({self.publ_year})'
    
    def __repr__(self):
        return f'{self.tittle} {self.publ_year} {self.genre} {self.views_number}'


class Series (Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        
    
    def __str__(self):
        if self.season <10:
            season_no = f'S0{self.season}'
        else:
            season_no = f'S0{self.season}'

        if self.episode <10:
            episode_no = f'E0{self.episode}'
        else:
            episode_no = f'E{self.episode}'
        return f'{self.tittle} {season_no} {episode_no}'
        
    def __repr__(self):
        return f'{self.tittle} {self.publ_year} {self.genre} {self.episode} {self.season} {self.views_number}'

serial_1 = Series(tittle = 'Friends', publ_year = 1994, genre ='comedy', episode =3, season = 10, views_number = 374)
film_1 = Movie (tittle = 'Lord of Rings', publ_year = 2003, genre = 'fantasy', views_number = 700)
serial_2 = Series(tittle = 'Stranger Things', publ_year = 2019, genre='fantasy', episode = 5, season = 3, views_number = 255)
fiilm_2 = Movie (tittle = 'We re the Millers', publ_year = 2003, genre = 'comedy', views_number = 500)
serial_3 = Series(tittle = 'Broadchurch', publ_year = 2013, genre = 'drama', episode=13, season=1, views_number = 197)
film_3 = Movie (tittle = 'Django', publ_year = 2012, genre = 'western', views_number = 648) 
library.append(serial_1)
library.append(film_1)
library.append(serial_2)
library.append(fiilm_2)
library.append(serial_3)
library.append(film_3)
movie_list = []
series_list = []

def get_movies():
    for position in library:
        if type(position) is Movie:
            movie_list.append(position)
        else:
            pass
    sorted_movie_list = sorted(movie_list, key = attrgetter('tittle'))
    return sorted_movie_list

def get_series():
    for position in library:
        if type(position) is Series:
            series_list.append(position)
        else:
            pass
    sorted_series_list = sorted(series_list, key = attrgetter('tittle'))
    return sorted_series_list

def search(give_tittle):
    for name in library:
        if name.tittle == give_tittle:
            return name

def generate_views():
    element = random.choice(library)
    element.views_number += random.randint(0,100)
    return (element.tittle, element.views_number)

def generate_views_10():
    for i in range(10):
        print(generate_views()) #kiedy uzywam "return" nie zwraca mi funkcji 10 razy, tylko raz. Jednak z funkcja print na koniec printuje "None"

def top_tittle(top):
    sorted_library = sorted(library, key = attrgetter('views_number'), reverse = True)
    return sorted_library[0:top]

#check
print(get_movies())
print(get_series())
print(search('Friends'))
print(search('Django'))
print(generate_views())
print(generate_views_10())
print(top_tittle(3))











