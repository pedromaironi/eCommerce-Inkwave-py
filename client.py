from base import DatabaseConnection
from clicks import Clicks
from product import Product
import traceback
import traceback


class Client:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_client_info(self, id_client):
        try:
            query = "SELECT id, nombre, fecha_registro, genero, direccion, edad, color_preferido, marca_favorita, talla_favorita, precio_preferido, categoria_preferida FROM cliente WHERE id = ?"
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
                    "talla_favorita": client_data[0][8],
                    "precio_preferido": client_data[0][9],
                    "categoria_preferida": client_data[0][10]
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
        self.product_instance = Product()
        self.user_profile = []

    def build_user_profile(self, id_client):
        try:
            client_info = self.client_instance.get_client_info(id_client)

            if client_info:
                # user_gender = client_info["genero"]
                # user_age = client_info["edad"]
                user_color_preference = client_info["color_preferido"]
                user_brand_preference = client_info["marca_favorita"]
                user_size_preference = client_info["talla_favorita"]
                user_price_preference = client_info["precio_preferido"]
                user_category_preference = client_info["categoria_preferida"]
                self.user_profile = [{                    # "gender": user_gender,
                    # "age": user_age,
                    "color": user_color_preference,
                    'brand': user_brand_preference,
                    'size': user_size_preference,
                    'price': user_price_preference,
                    'category': user_category_preference,
                }
                ]

                return self.user_profile
            else:
                print("Client information not found.")
                return None

        except Exception as e:
            print("Error:", e)

    def build_user_profile_clicks(self, id_client):
        try:
            clicks_instance = Clicks()
            client_info = self.client_instance.get_client_info(id_client)

            if client_info:
                user_id = id_client
                user_clicks_history = clicks_instance.get_user_clicks(
                    id_client)
                self.user_profile = [
                    user_id,
                    user_clicks_history
                ]

                return self.user_profile
            else:
                print("Client information not found.")
                return None

        except Exception as e:
            print("Error:", e)

    def recommend_products_based_on_clicks(self, id_client, num_recommendations=5):
        try:
            clicks_instance = Clicks()
            most_clicked_product_id = clicks_instance.get_user_clicks(
                id_client)

            if most_clicked_product_id:
                most_clicked_product_category = self.product_instance.get_product_info_list(
                    most_clicked_product_id)['categoria']

                recommendations = self.product_instance.get_products_by_category(
                    most_clicked_product_category, num_recommendations)

                recommended_product_ids = [product['id']
                                           for product in recommendations]
                return recommended_product_ids
            else:
                print("User click history not found.")
                return []

        except Exception as e:
            print("Error:", e)
