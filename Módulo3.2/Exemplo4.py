class Timer:
    def __init__(self, horas, minutos, segundos):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    def __str__(self):
        return self.create_template_datetime()
        
    def create_template_datetime(self):
        if self.__segundos < 10 and self.__minutos < 10 and self.__horas < 10:
             return f"0{self.__horas}:0{self.__minutos}:0{self.__segundos}"
        return f"{self.__horas}:{self.__minutos}:{self.__segundos}"
        
    def next_second(self):
        if self.__segundos >= 0 and self.__segundos < 59 and self.__horas < 23:
            self.__segundos += 1
        elif self.__segundos == 59 and self.__minutos < 59 and self.__horas < 23:
            self.__segundos = 0
            self.__minutos += 1
        elif self.__segundos == 59 and self.__minutos == 59 and self.__horas == 23:
            self.__segundos = 0
            self.__minutos = 0
            self.__horas = 0
        
    def prev_second(self):
        if self.__segundos == 0 and self.__minutos == 0 and self.__horas == 0:
            self.__segundos = 59
            self.__minutos = 59
            self.__horas = 23
        elif self.__segundos == 0 and self.__minutos == 0 and self.__horas <= 23:
            self.__segundos = 59
            self.__minutos = 59
            self.__horas -= 1
        elif self.__segundos == 0 and self.__minutos <= 59 and self.__horas <= 23:
            self.__segundos = 59
            self.__minutos -= 1
        elif self.__segundos <=59 and self.__minutos <= 59 and self.__horas <= 23:
            self.__segundos -= 1
            
            
        

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)