from product import Product
from clicks import Clicks
from client import UserProfileBuilder, Client
from base import DatabaseConnection
from ContentBasedRecommender import ContentBasedRecommender
import traceback

from categories import Categories
from brands import Brands
from sizes import Sizes


def main(id_client):
    db_connection = DatabaseConnection()
    try:
        # Obtén los perfiles de productos y los datos de clicks
        product_instance = Product()
        click_instance = Clicks()
        client_instance = Client()
        sizes_instance = Sizes()
        categories_instance = Categories()
        brands_instance = Brands()
        profile_builder = UserProfileBuilder()

        user_profile = profile_builder.build_user_profile(id_client)

        product_profiles = product_instance.create_product_profiles(id_client)

        recommender = ContentBasedRecommender(product_profiles)

        recommendations = recommender.recommend_products(user_profile)

        recommendations_minmax, recommendations_zscore = recommender.recommend_products(
            user_profile)

        # print("Product recommendations with Min-Max Scaling:")
        # for i, (product_id, similarity) in enumerate(recommendations_minmax[:5], 1):
        # print(f"{i}. Product ID: {product_id}, Similarity: {similarity}")

        top_5_minmax = [product_id for product_id,
                        _ in recommendations_minmax[:5]]

        return top_5_minmax
        # print("Product recommendations with Z-score normalization:")
        # for product_id, similarity in recommendations_zscore:
        #     print(f"Product ID: {product_id}, Similarity: {similarity}")
        # product_ids = [product_id for product_id, _ in recommendations]

        # similarity_matrix = recommender.calculate_similarity_matrix(
        #     user_profile)

        # print("Similarity matrix:")
        # for product_id, similarity_scores in zip(product_ids, similarity_matrix):
        #     print(
        #         f"Product ID: {product_id}, Similarities: {similarity_scores}")

        # for profile in recommender.product_features:
        # print(user_profile)
        #     print("------------------------")
        # print(user_profile[0])
        # for profile in recommender.product_features:
        #     print(profile)
        #     print("------------------------")
        # print(type(recommender._create_product_features()), type(user_profile))
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
