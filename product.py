from base import DatabaseConnection
from clicks import Clicks
from client import Client


class ProductProfileBasedContent:
    def __init__(self, product_id, color, brand, size, price, category):
        self.product_id = product_id
        self.price = price
        self.category = category
        self.brand = brand
        self.size = size
        self.color = color


class Product:

    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.clicks_instance = Clicks()
        self.color_mapping = {
            "celeste": 1,
            "negro": 2,
            "blanco": 3,
            "verde": 4,
            "variado": 5,
            "azul": 6,
            "gris": 7,
            "rojo": 8,
            "beige": 9,
            "rojo": 10
        }

    def get_all_products(self, id_client):
        try:
            query = "EXEC GetProductDetailsByClient @id_cliente = ?"
            product_data = self.db_connection.execute_query(query, id_client)

            products = []
            for row in product_data:
                product_info = {
                    "product_id": row[0],
                    "name": row[1],
                    "description": row[2],
                    "price": row[3],
                    "image": row[4],
                    "stock": row[5],
                    "category": row[6],
                    "color": self.color_mapping.get(row[10], 0),
                    "brand": row[11],
                    "size": row[14],
                    "favorite": (row[17]),
                    "clicks": float(row[18]),
                    "calification": (row[19])
                }
                products.append(product_info)

            return products

        except Exception as e:
            print("Error:", e)

    def create_product_profiles(self, id_client):
        try:
            click_rates_data = self.clicks_instance.calculate_click_rates(
                id_client)
            product_data = self.get_all_products(id_client)

            product_profiles = []
            for row in product_data:
                product_id = row["product_id"]
                price = row["price"]
                category = row["category"]
                color = row["color"]
                brand = row["brand"]
                size = row["size"]

                product_profiles.append(ProductProfileBasedContent(product_id,
                                                                   color, brand,
                                                                   size, price, category,
                                                                   ))
            return product_profiles
        except Exception as e:
            print("Error:", e)
