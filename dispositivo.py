

class Dispositivo:

    def __init__(self, id=0, nombre='', marca='', tipo=''):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.tipo = tipo

    def __repr__(self):
        return f"{self.id} - {self.nombre} - {self.marca} - {self.tipo}"

    def generate(self, object):
        for key in object:
            if key == 'id':
                self.id = object[key]
            elif key == 'nombre':
                self.nombre = object[key]
            elif key == 'marca':
                self.marca = object[key]
            elif key == 'tipo':
                self.tipo = object[key]