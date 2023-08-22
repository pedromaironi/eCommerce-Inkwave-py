from base import DatabaseConnection


class Categories:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_categories(self):
        try:
            query = "SELECT id, nombre, descripcion from Categoria"
            categories_data = self.db_connection.execute_query(
                query, 0)
            return categories_data

        except Exception as e:
            print("Error:", e)

    def get_category_by_id(self, category_id):
        try:
            query = "SELECT id, nombre, descripcion from Categoria where id = ?"
            categories_data = self.db_connection.execute_query(
                query, category_id)
            return categories_data

        except Exception as e:
            print("Error:", e)
