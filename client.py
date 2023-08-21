from base import DatabaseConnection
import traceback


class Client:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_client_info(self, id_client):
        try:
            query = "SELECT id, nombre, fecha_registro, genero, direccion, edad, color_preferido, marca_favorita, talla_favorita FROM cliente WHERE id = ?"
            client_data = self.db_connection.execute_query(
                query, id_client)

            # Preprocess data
            if client_data:
                client_info = {
                    "id": client_data[0][0],
                    "nombre": client_data[0][1],
                    "fecha_registro": client_data[0][2],
                    "genero": client_data[0][3],
                    "direccion": client_data[0][4],
                    "edad": client_data[0][5],
                    "color_preferido": client_data[0][6],
                    "marca_favorita": client_data[0][7],
                    "talla_favorita": client_data[0][8]
                }
                return client_info

            else:
                return None

        except Exception as e:
            print("Error:", e)
            traceback.print_exc()  # Print the traceback information


class UserProfileBuilder:
    def __init__(self):
        self.client_instance = Client()

    def build_user_profile(self, id_client):
        try:
            client_info = self.client_instance.get_client_info(id_client)

            if client_info:
                user_gender = client_info["genero"]
                user_age = client_info["edad"]
                user_color_preference = client_info["color_preferido"]
                user_brand_preference = client_info["marca_favorita"]
                user_size_preference = client_info["talla_favorita"]
                user_profile = {
                    "gender": user_gender,
                    "age": user_age,
                    "color_preference": user_color_preference,
                    "brand_preference": user_brand_preference,
                    "size_preference": user_size_preference
                }

                return user_profile
            else:
                print("Client information not found.")
                return None

        except Exception as e:
            print("Error:", e)
