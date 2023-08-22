from base import DatabaseConnection


class Brands:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_brands(self):
        try:
            query = "SELECT id, nombre, descripcion from marca"
            brands_data = self.db_connection.execute_query(
                query, 0)
            return brands_data

        except Exception as e:
            print("Error:", e)

    def get_brand_by_id(self, id):
        try:
            query = "SELECT id, nombre, descripcion from marca where id = ?"
            brands_data = self.db_connection.execute_query(
                query, id)
            return brands_data

        except Exception as e:
            print("Error:", e)
