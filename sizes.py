from base import DatabaseConnection


class Sizes:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_sizes(self):
        try:
            query = "SELECT id, nombre, descripcion from Talla"
            sizes_data = self.db_connection.execute_query(
                query)
            return sizes_data

        except Exception as e:
            print("Error:", e)
