from product import Product
from clicks import Clicks
from client import UserProfileBuilder, Client
from base import DatabaseConnection
from ContentBasedRecommender import ContentBasedRecommender
import traceback


def main(id_client):
    db_connection = DatabaseConnection()
    try:
        # Obtén los perfiles de productos y los datos de clicks
        product_instance = Product()
        click_instance = Clicks()
        client_instance = Client()
        profile_builder = UserProfileBuilder()

        user_profile = profile_builder.build_user_profile(id_client)

        product_profiles = product_instance.create_product_profiles(id_client)

        recommender = ContentBasedRecommender(product_profiles)

        recommendations = recommender.recommend_products(user_profile)

        print("Product recommendations:")
        for product_id, similarity in recommendations:
            print(f"Product ID: {product_id}, Similarity: {similarity}")

        print(product_profiles)
    except Exception as e:
        print("An error occurred:", e)
        return traceback.print_exc()
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
