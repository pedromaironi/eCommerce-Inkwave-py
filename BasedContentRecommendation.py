from product import Product
from clicks import Clicks
from client import UserProfileBuilder, Client
from base import DatabaseConnection
from Recommender import Recommender
import traceback
import sys
import numpy as np
from categories import Categories
from brands import Brands
from sizes import Sizes


class BasedContentRecommendation:

    def __init__(self, id_client):
        self.id_client = id_client
        self.db_connection = DatabaseConnection()
        self.generateRecommendation(self.id_client)

    def generateRecommendation(self, id_client):
        try:
            product_instance = Product()
            click_instance = Clicks()
            client_instance = Client()
            sizes_instance = Sizes()
            categories_instance = Categories()
            brands_instance = Brands()
            profile_builder = UserProfileBuilder()

            user_profile = profile_builder.build_user_profile(id_client)

            # product_profiles = product_instance.create_product_profiles(
            #     id_client)

            # recommender_ = Recommender(product_profiles)

            # # recommendations = recommender_.recommend_products(user_profile)

            # recommendations_minmax, recommendations_zscore = recommender_.recommend_products(
            #     user_profile)
            product_list = self.get_matching_products(user_profile)
            seen_product_ids = set()
            unique_product_list = []

            for product in product_list:
                product_id = product['id']
                if product_id not in seen_product_ids:
                    unique_product_list.append(product)
                    seen_product_ids.add(product_id)

            for product in unique_product_list:
                print(product['id'])
            # print(user_profile[0]['color'])

        except Exception as e:
            print("An error occurred:", e)
            return traceback.print_exc()
        finally:
            self.db_connection.close()

    def get_matching_products(self, user_profile):
        try:
            query = """
            SELECT p.id, p.nombre, c.nombre AS categoria, m.nombre AS marca, p.precio, cc.cantidad_clicks
            FROM producto AS p
            JOIN categoria AS c ON p.id_categoria = c.id
            JOIN detalleProducto AS dp ON p.id = dp.id_producto
            JOIN marca AS m ON dp.id_marca = m.id
            JOIN Clicks as cc ON p.id = cc.id_producto
            WHERE dp.color = ? 
              AND m.nombre = ? 
              AND dp.id_talla = ?
              AND p.precio <= ?
              AND c.nombre = ?
            ORDER BY cc.cantidad_clicks DESC
                """

            color = user_profile[0]['color']
            brand = user_profile[0]["brand"]
            size = user_profile[0]["size"]
            price = user_profile[0]["price"]
            category = user_profile[0]["category"]
            product_data = self.db_connection.execute_large_query(
                query, (color, brand, size, price, category))

            # Preprocess data
            product_list = []
            for row in product_data:
                product_info = {
                    "id": row[0],
                    "nombre": row[1],
                    "categoria": row[2],
                    "marca": row[3],
                    "precio": row[4],
                    "cantidad_clicks": row[5]
                }
                product_list.append(product_info)

            return product_list

        except Exception as e:
            print("Error:", e)
            traceback.print_exc()  # Print the traceback information


if len(sys.argv) > 1:
    id_client = sys.argv[1]
    recommendation_instance = BasedContentRecommendation(id_client)
