class WeekDayError(Exception):
    pass
	

class Weeker:
    

    def __init__(self, day):
        if day not in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
            raise WeekDayError()
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        semana = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        index = 0
        day = 0
        dias_semana = len(semana)
        while day < n:
            index = (index + 1) % dias_semana
            self.__day = semana[index]
            day += 1

    def subtract_days(self, n):
        semana = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        index = 0
        day = 0
        dias_semana = len(semana)
        while day < n:
            self.__day = semana[index]
            index = (index - 1) % dias_semana
            day += 1        


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")