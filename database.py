
from dispositivo import Dispositivo

class Database:

    def __init__(self, template):
        self.template = template
        self.database = self.generateDatabase()

    def generateDatabase(self):
        auxiliar = []
        for each in self.template['dispositivos']:
            dispositivo = Dispositivo()
            dispositivo.generate(each)
            auxiliar.append(dispositivo)
        return auxiliar
    
    def delete_by_id(self, id):
        auxiliar = []
        for i in range(len(self.database)):
            each = self.database[i]
            if not each.id == id:
                auxiliar.append(each)
        self.database = auxiliar

    def add_dispositivo(self, dispositivo: Dispositivo):
        self.database.append(dispositivo)
        
