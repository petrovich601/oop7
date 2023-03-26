from Drink import Drink


class Hot_Drink(Drink):
    def __init__(self, title, date, weight):
        super().__init__(title)
        self._date = date
        self._weight = weight

    @property
    def date(self):
        return self._date

    @property
    def weight(self):
        return self._weight

    @date.setter
    def date(self, new_date):
        self._date = new_date

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    def __str__(self) -> str:
        return f" напиток: {self.title} цена: {self._date} объем: {self._weight}"