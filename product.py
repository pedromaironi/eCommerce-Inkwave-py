from base import DatabaseConnection
from clicks import Clicks
import traceback


class ProductProfileBasedContent:
    def __init__(self, product_id, color, brand, size, price, category):
        self.product_id = product_id
        self.price = price
        self.category = category
        self.brand = brand
        self.size = size
        self.color = color


class ProductProfileClicks:
    def __init__(self, product_id, clicks):
        self.product_id = product_id
        self.clicks = clicks


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

    def get_product_info_list(self, product_id):
        try:
            query = """
            SELECT p.id, p.nombre, c.nombre AS categoria, m.nombre AS marca, p.precio, cc.cantidad_clicks
            FROM producto AS p
            JOIN categoria AS c ON p.id_categoria = c.id
            JOIN detalleProducto AS dp ON p.id = dp.id_producto
            JOIN marca AS m ON dp.id_marca = m.id
			JOIN Clicks as cc ON p.id = cc.id_producto
            where p.id = ?
            """
            product_data = self.db_connection.execute_query(query, product_id)

            # Preprocess data
            if product_data:
                product_info = {
                    "id": product_data[0][0],
                    "nombre": product_data[0][1],
                    "categoria": product_data[0][2],
                    "marca": product_data[0][3],
                    "precio": product_data[0][4],
                    "cantidad_clicks": float(product_data[0][5])
                }
                return product_info
            else:
                return None

        except Exception as e:
            print("Error:", e)
            traceback.print_exc()  # Print the traceback information

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

    def create_product_clicks_profile(self, id_client):
        try:
            product_data = self.get_all_products(id_client)

            product_profiles = []
            for row in product_data:
                product_id = row["product_id"]
                clicks = row["clicks"]

                product_profiles.append(
                    ProductProfileClicks(product_id, clicks))
            return product_profiles
        except Exception as e:
            print("Error:", e)

    def get_products_by_category(self, category_name, num_products=5):
        try:
            query = """
            SELECT p.id, p.nombre, c.nombre AS categoria, m.nombre AS marca, p.precio, cc.cantidad_clicks
            FROM producto AS p
            JOIN categoria AS c ON p.id_categoria = c.id
            JOIN detalleProducto AS dp ON p.id = dp.id_producto
            JOIN marca AS m ON dp.id_marca = m.id
            JOIN Clicks as cc ON p.id = cc.id_producto
            WHERE c.nombre = ?
            ORDER BY cc.cantidad_clicks DESC
            """

            product_data = self.db_connection.execute_query(
                query, (category_name))

            # Preprocess data
            product_list = []
            for row in product_data:
                product_info = {
                    "id": row[0],
                    "nombre": row[1],
                    "categoria": row[2],
                    "marca": row[3],
                    "precio": row[4],
                    "cantidad_clicks": row[5]
                }
                product_list.append(product_info)

            return product_list

        except Exception as e:
            print("Error:", e)
            traceback.print_exc()  # Print the traceback information
