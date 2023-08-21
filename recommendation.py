import searches
import sys
id_usuario = sys.argv[1]


def generate_recommendations(id_usuario):
    try:
        # Retrieve data using data classes
        data = searches.get_searches(id_usuuario)

        recommendations = "Recommendations for user " + \
            str(id_usuario) + data
        return recommendations
    except Exception as e:
        print("An error occurred:", e)
        return "An error occurred while generating recommendations."
