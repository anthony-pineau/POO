from datetime import datetime

class DateProcessor:
    def process_date(self, date_str):
        date = datetime.strptime(date_str, "%Y-%m-%d")  # Convertir la chaîne de caractères en objet datetime
        month = date.strftime("%B")
        month_number = date.month
        year = date.year
        day = date.day

        return (date_str, month, month_number, year, day)

class DateGenerator(DateProcessor):
    def __init__(self):
         self._dates = []
         self._listDate = []

    def get_dates(self):
        return self._dates
      
    def set_dates(self, x):
        self._dates.append(x)
    
    def get_listDate(self):
        return self._listDate
      
    def set_listDate(self, x):
        self._listDate.append(x)

    def generate_date(self):
        dates = self.get_dates()
        strListeDate = []

        for date_str in dates:
            processed_date = self.process_date(date_str)
            strListeDate.extend(processed_date)

        self.set_listDate(strListeDate)
