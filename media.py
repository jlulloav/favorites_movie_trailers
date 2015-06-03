import webbrowser

class Movie():
    """Stores a movie information

    Attributes:
        title: A string with the movie title.
        storyline: A string with the movie storyline.
        poster_image_url: A string with the movie-poster-image url.
        trailer_youtube_url: A string with the movie-trailer-youtube url.
        director_name: A string with the movie-director name.
        featured_song: A string indicating the movie-featured song.
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_director_name, movie_featured_song):
        """Inits Movie with title, storyline, poster image url,
        trailer youtube url, director name, and release date"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director_name = movie_director_name
        self.featured_song = movie_featured_song

    def show_trailer(self):
        """Opens the trailer youtube url in a web browser"""
        webbrowser.open(self.trailer_youtube_url)
