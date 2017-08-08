import webbrowser


class Movie():
    """Movie object class.
       Has a constructor and a function to show the movie's trailer"""
    # Constructor class for Movie
    def __init__(self, title, storyline,
                 poster_image_url, trailer_youtube_url):
        """Movie class constructor.\n
           Must be initialized with a title, storyline, poster image (url)
           and a link to its trailer (url)"""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # Opens a web browser showing the movie's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
