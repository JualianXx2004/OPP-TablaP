
#Crear la clase
class Periodica():
    #Utilizar el metodo constructor
    def __init__(self,estado):
        self.simbolo = "H"
        self.nombre = "Hidrogeno"
        self.estado = estado
        self.numatm = 1
        self.pesatom = 1 
        
    def infor(self):
        print("El Hidrogeno es el primero elemento de latabla periodica. Es el elemento mas ligero que existe, su atomo esta formado por un proton y un electron")

       
    def mostrar_datos(self): 
        print("DATOS DEL ELEMENTO")
        print("Nombre del elemento:", self.nombre)
        print("Simbolo:", self.simbolo)
        print("Numero atomico:", self.numatm)
        print("Su estado es:", self.estado)
        print("Peso atomico es:", self.pesatom)

print()      
class Periodi():

    def __init__(self,estadoo):
        self.simbolo = "Cl"
        self.nombre = "Cloro"
        self.estadoo = estadoo
        self.numatm = 17
        self.pesatom = 35.45
        
    def inforr(self):
        print("Si el cloro es liberado al agua o al suelo o si se escapa al aire desde un tanque, se evaporará rápidamente formando una nube verde-amarillenta que puede ser movilizada por el viento lejos de la fuente original.")
        
    def mostrar_datoss(self): 
        print("DATOS DEL ELEMENTO")
        print("Nombre del elemento:", self.nombre)
        print("Simbolo:", self.simbolo)
        print("Numero atomico:", self.numatm)
        print("Su estado es:", self.estadoo)
        print("Peso atomico es:", self.pesatom)

print()
class Period():

    def __init__(self,estado):
        self.simbolo = "C"
        self.nombre = "Carbono"
        self.estado = estado
        self.numatm = 6
        self.pesatom = 12
        
    def infoorr(self):
        print("El uso más extendido del carbono es como componente en los hidrocarburos, sobre todo los combustibles fósiles como el petróleo para producir gasolinas, aceites, o como materia prima para producir plásticos, o el gas natural que se está imponiendo como fuente de energía más limpia.")
        
    def mostrar_datosss(self): 
        print("DATOS DEL ELEMENTO")
        print("Nombre del elemento:", self.nombre)
        print("Simbolo:", self.simbolo)
        print("Numero atomico:", self.numatm)
        print("Su estado es:", self.estado)
        print("Peso atomico es:", self.pesatom)





        
#Instanciar la clase
per = Periodica("Solido, liquido y gaseoso")
per.mostrar_datos()
print()
per.infor()
print()
perr = Periodi("Liquido")
perr.mostrar_datoss()
print()
perr.inforr()
print()
perrr = Period("Solido")
perrr.mostrar_datosss()
print()
perrr.infoorr()




