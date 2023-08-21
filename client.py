from base import DatabaseConnection


class Client:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_client_info(self, id_client):
        try:
            query = "SELECT id, nombre, fecha_registro, genero, direccion, edad, estilo_preferido, color_preferido, marcas_favoritas, talla FROM cliente WHERE id = ?"
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


class UserProfileBuilder:
    def __init__(self, id_client):
        self.id_client = id_client
        self.client_instance = Client()

    def build_user_profile(self):
        try:
            client_info = self.client_instance.get_client_info(self.id_client)

            if client_info:
                user_gender = client_info["genero"]
                user_age = client_info["edad"]
                user_style_preference = client_info["estilo_preferido"]
                user_color_preference = client_info["color_preferido"]
                user_brand_preference = client_info["marcas_favoritas"]
                user_size_preference = client_info["talla"]

                user_profile = {
                    "gender": user_gender,
                    "age": user_age,
                    "style_preference": user_style_preference,
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
