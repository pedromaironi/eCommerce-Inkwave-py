from product import Product
from clicks import Clicks
from client import Client
from base import DatabaseConnection
from sklearn.metrics.pairwise import cosine_similarity


def main(id_client):
    db_connection = DatabaseConnection()
    try:
        # Obtén los perfiles de productos y los datos de clicks
        product_instance = Product()
        click_instance = Clicks()
        client_instance = Client()

        product_profiles = product_instance.create_product_profiles(id_client)
        click_rates = click_instance.calculate_click_rates(id_client)

        client_info = client_instance.get_client_info(id_client)
        user_gender = client_info["genero"]
        user_age = client_info['edad']
        user_style_preference = client_info["estilo_preferido"]
        user_color_preference = client_info["color_preferido"]
        user_brand_preference = client_info["marcas_favoritas"]
        user_size_preference = client_info["talla"]

        # Crea un perfil de usuario de ejemplo (puedes adaptarlo según tus necesidades)
        user_profile = [user_gender. user_age,
                        user_style_preference,
                        user_color_preference,
                        user_brand_preference,
                        user_size_preference,
                        ]

    except Exception as e:
        print("An error occurred:", e)
        return "An error occurred while generating recommendations."
    finally:
        db_connection.close()


if __name__ == "__main__":
    import sys
    import numpy as np

    if len(sys.argv) > 1:
        id_client = sys.argv[1]
        main(id_client)
    else:
        print("Please provide an id_client as an argument.")
