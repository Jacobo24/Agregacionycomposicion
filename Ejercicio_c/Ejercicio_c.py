#La clase cristal, ventana y paredcortina me las ha dado chatgpt

class Cristal:
    def __init__(self, transparencia):
        self.transparencia = transparencia

class Ventana:
    def __init__(self, cristal):
        self.cristal = cristal

class ParedCortina:
    def __init__(self, cristal, ventanas=[]):
        self.cristal = cristal
        self.ventanas = ventanas


    def set_transparencia(self, nueva_transparencia):
        self.cristal.set_transparencia(nueva_transparencia)

def set_transparencia(self, nueva_transparencia):
    self.transparencia = nueva_transparencia
    self.cristal.set_transparencia(nueva_transparencia)
    for ventana in self.ventanas:
        ventana.set_transparencia(nueva_transparencia)

cristal_pared = Cristal(80)
ventana1 = Ventana(Cristal(50))
ventana2 = Ventana(Cristal(70))

pared_cortina = ParedCortina(cristal_pared, [ventana1, ventana2])

ventana1.set_transparencia(40)
ventana2.set_transparencia(60)
pared_cortina.set_transparencia(90)
