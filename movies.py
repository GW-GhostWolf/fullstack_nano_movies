import webbrowser


class Movie():
    """
    Container for basic movie information
        Title
        Storyline
        Poster Image
        Trailer Link
    """
    def __init__(self, title, story, image, trailer):
        """
        Constructor for Movie class
            Input: title - Movie Title
            Input: story - Storyline for the movie
            Input: image - URL for a poster image
            Input: trailer - URL for the movie trailer on youtube.com
            Output: Instantiated movie object
        """
        self.title = title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """
        Show the movie's trailer
        """
        webbrowser.open(self.youtube_trailer)
