class Movies:
    def __init__(self):
        self.movies = []
    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: '{self.movies}'"

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: '{self.movies}'"

comedy_instance = Comedy()
print(comedy_instance.add_movie("Большой куш"))

drama_instance = Drama()
print(drama_instance.add_movie("Оружейный барон"))