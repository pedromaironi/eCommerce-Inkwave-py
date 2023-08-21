class ProductProfile:
    def __init__(self, product_id, category, price, brand, description, average_rating):
        self.product_id = product_id
        self.category = category
        self.price = price
        self.brand = brand
        self.description = description
        self.average_rating = average_rating
        self.clicks = 0  # Se inicializa en cero, se actualizará con los datos de clics
        self.related_products = []  # Se actualizará con productos relacionados

    def update_clicks(self, clicks):
        self.clicks = clicks

    def add_related_product(self, product_id):
        self.related_products.append(product_id)

    def __str__(self):
        return f"Product ID: {self.product_id}\n" \
               f"Category: {self.category}\n" \
               f"Price: {self.price}\n" \
               f"Brand: {self.brand}\n" \
               f"Description: {self.description}\n" \
               f"Average Rating: {self.average_rating}\n" \
               f"Clicks: {self.clicks}\n" \
               f"Related Products: {self.related_products}\n"
