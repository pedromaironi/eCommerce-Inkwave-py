from base import DatabaseConnection
from clicks import Clicks
from client import Client


class ProductProfileBasedContent:
    def __init__(self, product_id, product_name, description, price, category, brand,
                 size, favorite, total_clicks, average_rating, color, cliente_info):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.category = category
        self.brand = brand
        self.size = size
        self.favorite = favorite
        self.total_clicks = total_clicks
        self.average_rating = average_rating
        self.color = color
        self.cliente_info = cliente_info


class Product:

    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.clicks_instance = Clicks()

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
                    "category": row[7],
                    "color": row[10],
                    "brand": row[12],
                    "size": row[15],
                    "favorite": bool(row[17]),
                    "clicks": row[18],
                    "calificacion": row[19]
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
            client_instance = Client()

            product_profiles = []
            for row in product_data:
                product_id = row["product_id"]
                product_name = row["name"]
                description = row["description"]
                price = row["price"]
                category = row["category"]
                brand = row["brand"]
                size = row["size"]
                favorite = row["favorite"]
                total_clicks = row["clicks"]
                average_rating = row["calificacion"]
                color = row["color"]
                client_info = client_instance.get_client_info(id_client)

                product_profiles.append(ProductProfileBasedContent(
                    product_id, product_name, description,
                    price, category, brand,
                    size, favorite, total_clicks, average_rating, color, client_info
                ))

            return product_profiles

        except Exception as e:
            print("Error:", e)
