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

            # Now you have a nested dictionary 'user_click_rates' that maps user IDs to product click rates
            return click_rates_data

        except Exception as e:
            print("Error:", e)

    def get_user_clicks(self, id_client):
        try:
            query = """ SELECT TOP 1 id_producto, cantidad_clicks
                        FROM clicks
                        WHERE id_cliente = ?
                        ORDER BY cantidad_clicks DESC;
                    """
            clicks_data = self.db_connection.execute_query(query, id_client)

            # Extract product IDs from clicks data
            user_click_history = [click[0] for click in clicks_data]
            return user_click_history

        except Exception as e:
            print("Error:", e)
            return []
