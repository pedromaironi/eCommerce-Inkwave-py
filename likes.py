from base import DatabaseConnection


class Likes:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_likes(self, id_client):
        try:
            query = "SELECT id_favorito, id_cliente, id_producto, fecha_favorito FROM Favoritos WHERE id_cliente = ?"
            likes_data = self.db_connection.execute_query(
                query, id_client)

            # Preprocess data
            user_likes = {}  # Dictionary to store user's favorite products
            for like_id, user_id, product_id, _ in likes_data:
                if user_id not in user_likes:
                    user_likes[user_id] = []
                user_likes[user_id].append(product_id)

            # Now you have a dictionary 'user_likes' that maps users to their favorite products
            return user_likes

        except Exception as e:
            print("Error:", e)
