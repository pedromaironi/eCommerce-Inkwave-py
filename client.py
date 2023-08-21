from base import DatabaseConnection


class Client:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_client_info(self, id_client):
        try:
            query = "SELECT id, nombre, fecha_registro, genero, direccion, estilo_preferido, color_preferido. marcas_favoritas, talla FROM cliente WHERE id = ?"
            client_data = self.db_connection.execute_query(
                query, id_client)

            # Preprocess data
            if client_data:
                client_info = {
                    "id": client_data[0],
                    "nombre": client_data[1],
                    "fecha_registro": client_data[2],
                    "genero": client_data[3],
                    "direccion": client_data[4],
                    "edad": client_data[5],
                    "estilo_preferido": client_data[6],
                    "color_preferido": client_data[7],
                    "marcas_favoritas": client_data[8],
                    "talla": client_data[9]
                }
                return client_info

            else:
                return None

        except Exception as e:
            print("Error:", e)
