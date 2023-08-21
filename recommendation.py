from searches import Searches
from likes import Likes
from clicks import Clicks


def generate_recommendations(id_client):
    try:
        # searches_instance = Searches()
        # likes_instance = Likes()
        clicks_instance = Clicks()
        # user_searches = searches_instance.get_searches(id_client)
        # user_likes = likes_instance.get_likes(id_client)
        user_clicks = clicks_instance.get_clicks(id_client)
        click_rates = clicks_instance.calculate_click_rates(id_client)
        clicks_instance.close_connection()

        recommendations = str(click_rates)
        return recommendations
    except Exception as e:
        print("An error occurred:", e)
        return "An error occurred while generating recommendations."


# Get the id_client from the command line
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        id_client = sys.argv[1]
        recommendation = generate_recommendations(id_client)
        print(recommendation)
    else:
        print("Please provide an id_client as an argument.")
