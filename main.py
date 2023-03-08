from dispositivo import Dispositivo
from database import Database

if __name__ == '__main__':

    database_template = {"dispositivos": [
            {
                "id": 1,
                "nombre": "teclado",
                "marca": "genius",
            },
            {
                "id": 2,
                "nombre": "mouse",
                "marca": "logitech",
            },
            {
                "id": 3,
                "nombre": "memoria",
                "tipo": "ram",
            }
    ]}

    dispositivo1 = Dispositivo(1, "teclado", "genius")
    dispositivo2 = Dispositivo(2, "mouse", "logitech")
    dispositivo3 = Dispositivo(3, "memoria", tipo="ram")
    dispositivo4 = Dispositivo(4, "placa de red", tipo="wireless", marca="tp-link")


    def compare_dispositivos(object1: Dispositivo, object2: Dispositivo):
        print(object1)
        print(object2)
        if object1.id != object2.id:
            return False
        if object1.nombre != object2.nombre:
            return False
        if object1.marca != object2.marca:
            return False
        if object1.tipo != object2.tipo:
            return False
        return True
    
    database = Database(database_template)
    result = compare_dispositivos(dispositivo1, database.database[1])
    print(result)
    database.delete_by_id(id=2)
    print(database.database)
