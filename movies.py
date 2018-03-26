import webbrowser


class Movie():
    """Hold the movie title, storyline, poster image URL, trailer URL"""
    def __init__(self, title, story, image, trailer):
        self.title = title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """Show the movie's trailer"""
        webbrowser.open(self.youtube_trailer)
