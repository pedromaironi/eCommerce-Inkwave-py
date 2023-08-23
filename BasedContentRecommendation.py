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

            product_profiles = product_instance.create_product_profiles(
                id_client)

            recommender_ = Recommender(product_profiles)

            # recommendations = recommender_.recommend_products(user_profile)

            recommendations_minmax, recommendations_zscore = recommender_.recommend_products(
                user_profile)

            for product_id, similarity in recommendations_minmax:
                print(product_id)

        except Exception as e:
            print("An error occurred:", e)
            return traceback.print_exc()
        finally:
            self.db_connection.close()


if len(sys.argv) > 1:
    id_client = sys.argv[1]
    recommendation_instance = BasedContentRecommendation(id_client)
