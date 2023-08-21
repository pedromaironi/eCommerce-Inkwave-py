from searches import Searches


def generate_recommendations(id_usuario):
    try:
        searches_instance = Searches()
        user_searches = searches_instance.get_searches(id_usuario)

        recommendations = "Recommendations for user " + \
            str(id_usuario) + str(user_searches)
        return recommendations
    except Exception as e:
        print("An error occurred:", e)
        return "An error occurred while generating recommendations."


# Get the id_usuario from the command line
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        id_usuario = sys.argv[1]
        recommendation = generate_recommendations(id_usuario)
        print(recommendation)
    else:
        print("Please provide an id_usuario as an argument.")
