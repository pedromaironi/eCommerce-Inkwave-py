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


class ClicksContentRecommendation:

    def __init__(self, id_client):
        self.id_client = id_client
        self.db_connection = DatabaseConnection()
        self.generateRecommendation(self.id_client)
        self.product = Product()
        # print(self.product.get_product_info_list(self.id_client))

    def generateRecommendation(self, id_client):
        try:
            product_instance = Product()
            click_instance = Clicks()
            client_instance = Client()
            sizes_instance = Sizes()
            categories_instance = Categories()
            brands_instance = Brands()
            profile_builder = UserProfileBuilder()

            user_profile = profile_builder.recommend_products_based_on_clicks(
                id_client)

            print(user_profile)

        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.db_connection.close()


if len(sys.argv) > 1:
    id_client = sys.argv[1]
    recommendation_instance = ClicksContentRecommendation(id_client)
