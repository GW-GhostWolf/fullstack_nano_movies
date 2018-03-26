import movies
import fresh_tomatoes

list_of_movies = [
    movies.Movie("Avatar", "Marine on an alien planet",
                 "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                 "https://www.youtube.com/watch?v=-9ceBgWV8io"),
    movies.Movie("Fantastic Beasts", "Magic creatures loose in New York City",
                 "https://upload.wikimedia.org/wikipedia/en/5/5e/Fantastic_Beasts_and_Where_to_Find_Them_poster.png",  # NOQA
                 "https://www.youtube.com/watch?v=ViuDsy7yb8M"),
    movies.Movie("Harry Potter", "You're a wizard, Harry",
                 "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG",  # NOQA
                 "https://www.youtube.com/watch?v=K1KPcXRMMo4"),
    movies.Movie("Hunger Games", "Deadly olympics for kids",
                 "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # NOQA
                 "https://www.youtube.com/watch?v=PbA63a7H0bo"),
    movies.Movie("Ratatouille", "Rat likes to cook",
                 "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # NOQA
                 "https://www.youtube.com/watch?v=c3sBBRxDAqk"),
    movies.Movie("School of Rock", "storyline for school of rock",
                 "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                 "https://www.youtube.com/watch?v=3PsUJFEBC74")
    ]

fresh_tomatoes.open_movies_page(list_of_movies)
