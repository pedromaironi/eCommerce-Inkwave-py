from product import Product
from base import DatabaseConnection


def generate_recommendations(id_usuario):
    db_connection = DatabaseConnection()
    try:
        clicks_instance = Product()
        user_clicks = clicks_instance.create_product_profiles(id_usuario)

        recommendations = str(user_clicks)
        for profile in user_clicks:
            print("Product ID:", profile.product_id)
            print("Product Name:", profile.product_name)
            # print("Description:", profile.description)
            # ... (imprime otros atributos)
            print("Total Clicks:", profile.total_clicks)
            print("Average Rating:", profile.average_rating)
            print("-----------------------")
    except Exception as e:
        print("An error occurred:", e)
        return "An error occurred while generating recommendations."
    finally:
        db_connection.close()


# Get the id_usuario from the command line
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        id_usuario = sys.argv[1]
        recommendation = generate_recommendations(id_usuario)
        print(recommendation)
    else:
        print("Please provide an id_usuario as an argument.")


# from recommendationEngine import RecommendationEngine

# if __name__ == "__main__":
#     import sys
#     try:
#         if len(sys.argv) > 1:
#             id_client = sys.argv[1]
#             recommendation_engine = RecommendationEngine()
#             recommendations = recommendation_engine.generate_recommendations(
#                 id_client)
#             print("Recommendations:", recommendations)

#     except Exception as e:
#         print("An error occurred:", e)
