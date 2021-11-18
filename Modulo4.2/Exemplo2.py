class ficheiro:
    def __init__(self):
        self.lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.histograma = dict()
    
    def __str__(self):
        for key in self.histograma:
            if self.histograma[key] > 0:
                print(f"{key} -> {self.histograma[key]}")
        return ""
    def get_histograma(self, input):
        input = input.lower()
        for letra in self.lista:
            value = input.count(letra)
            self.histograma[letra] = value    
        self.sort_histograma()
        
    def sort_histograma(self):   
        self.histograma = dict(sorted(self.histograma.items(), key=lambda x: x[1], reverse=True))
        
        
objetos = ficheiro()
objetos.get_histograma('cBabbAc')
print(objetos)