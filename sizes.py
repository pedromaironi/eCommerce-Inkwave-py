from base import DatabaseConnection


class Sizes:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_sizes(self):
        try:
            query = "SELECT id, nombre, descripcion from Talla"
            sizes_data = self.db_connection.execute_query(
                query, 0)
            return sizes_data

        except Exception as e:
            print("Error:", e)

    def get_size_by_id(self, id):
        try:
            query = "SELECT id, nombre, descripcion from Talla where id = ?"
            sizes_data = self.db_connection.execute_query(
                query, id)
            return sizes_data

        except Exception as e:
            print("Error:", e)
