"""Defines the class Movie """
import webbrowser


class Movie():
    """ This class provides a way to store movie related infomation. Like
        movie title, storyline, poster image URL and trailer URL from youtube.
     """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

"""uses the webbrowser module to open the youtube trailer in the browser"""


def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)

"""uses the webbrowser module to open the movie poster image in the browser"""


def show_poster(self):
    webbrowser.open(self.poster_image_url)
