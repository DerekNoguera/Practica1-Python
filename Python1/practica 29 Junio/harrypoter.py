class Magos:
    def __init__(self,nombres, hechizos, vida):
        self.nombre = nombres
        self.hechizos = hechizos
        self.vida = vida
        
    def id(self):
        print(f"Hechizo {self.hechizos} lanzado con exito ")
    
        
Harry_Potter = Magos(nombres="Harry Potter", hechizos='Demage', vida=100)
Gandalf = Magos( nombres='Gandalf', hechizos='Speed', vida=90)
Merlin = Magos( nombres='Merlin', hechizos='Fuerza', vida=96)

Harry_Potter.id()
Gandalf.id()
Merlin.id()