import webbrowser


class Movie():
    def __init__(self, title, story, image, trailer):
        self.title = title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)
