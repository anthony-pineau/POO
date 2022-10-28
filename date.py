import datetime

class DateGuesser():

    def __init__(self):
         self._dates = []
         self._month = []
         self._monthNumber = []
         self._year = []
         self._day = []
         self._listDate = []

    # getter method
    def get_dates(self):
        return self._dates
      
    # setter method
    def set_dates(self, x):
        self._dates.append(x)
    
    # getter method
    def get_month(self):
        return self._month
      
    # setter method
    def set_month(self, x):
        self._month.append(x)
    
    # getter method
    def get_monthNumber(self):
        return self._monthNumber
      
    # setter method
    def set_monthNumber(self, x):
        self._monthNumber.append(x)

    # getter method
    def get_year(self):
        return self._year
      
    # setter method
    def set_year(self, x):
        self._year.append(x)

    # getter method
    def get_day(self):
        return self._day
      
    # setter method
    def set_day(self, x):
        self._day.append(x)

    # getter method
    def get_listDate(self):
        return self._listDate
      
    # setter method
    def set_listDate(self, x):
        self._listDate.append(x)
      
guesser = DateGuesser()

date = datetime.date(2019, 4, 13)

guesser.set_dates(date)
guesser.set_month(date.strftime("%B"))
guesser.set_monthNumber(date.month)
guesser.set_year(date.year)
guesser.set_day(date.day)

print(date)
strListeDate = []
strListeDate += guesser.get_dates()
strListeDate += guesser.get_month()
strListeDate += guesser.get_monthNumber()
strListeDate += guesser.get_year()
strListeDate += guesser.get_day()
#strListeDate += guesser.get_dates().replace("-", "")

guesser.set_listDate(strListeDate)
