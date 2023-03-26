class Drink:
    def __init__(self, title):
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title



    def __str__(self):
        return self.title