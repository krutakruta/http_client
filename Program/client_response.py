class TextClientResponse:
    def __init__(self, text=None):
        self._text = text

    def set_text(self, text):
        self._text = text

    @property
    def text(self):
        return self._text
