from base import DatabaseConnection


class Clicks:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_clicks(self, id_client):
        try:
            query = "SELECT id_cliente, id_producto, fecha_click FROM Clicks WHERE id_cliente = ?"
            clicks_data = self.db_connection.execute_query(
                query, id_client)

            # Preprocess data
            user_clicks = {}  # Dictionary to store user's clicks on products
            for user_id, product_id, _ in clicks_data:
                if user_id not in user_clicks:
                    user_clicks[user_id] = []
                user_clicks[user_id].append(product_id)

            # Now you have a dictionary 'user_clicks' that maps users to products they clicked on
            return user_clicks

        except Exception as e:
            print("Error:", e)

    def calculate_click_rates(self, id_client):
        try:
            query = "SELECT id_cliente, id_producto, cantidad_clicks FROM Clicks WHERE id_cliente = ?"
            click_rates_data = self.db_connection.execute_query(
                query, id_client)

            # Calculate click rates
            user_click_rates = {}  # Dictionary to store user's product click rates
            for user_id, product_id, total_clicks in click_rates_data:
                if user_id not in user_click_rates:
                    user_click_rates[user_id] = {}
                user_click_rates[user_id][product_id] = total_clicks

            # Now you have a nested dictionary 'user_click_rates' that maps user IDs to product click rates
            return user_click_rates

        except Exception as e:
            print("Error:", e)

    def create_product_profiles(self, id_client):
        try:
            all_click_rates = self.clicks_instance.calculate_click_rates()

            # Si tienes otros atributos relevantes, obtenerlos de manera similar

            # Crear perfiles de productos
            product_profiles = []
            for product_id, click_rates in all_click_rates.items():
                # Crear un diccionario para el perfil del producto
                product_profile = {
                    "product_id": product_id,
                    "clicks": click_rates,
                    # Agregar otros atributos relevantes al diccionario
                }
                product_profiles.append(product_profile)

            return product_profiles
        except Exception as e:
            print("Error:", e)

    def close_connection(self):
        self.db_connection.close()
