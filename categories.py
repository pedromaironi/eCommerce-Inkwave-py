from base import DatabaseConnection


class Categories:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_sizes(self):
        try:
            query = "SELECT id, nombre, descripcion from Categoria"
            categories_data = self.db_connection.execute_query(
                query)
            return categories_data

        except Exception as e:
            print("Error:", e)
