class ContentBasedRecommendation:
    def __init__(self, product_profiles):
        self.product_profiles = product_profiles  # Diccionario de perfiles de productos

    def cosine_similarity(self, profile1, profile2):
        # Implementa la función de similitud del coseno como se mostró en la respuesta anterior
        # Puedes adaptarla según los atributos en tus perfiles y su formato

    def get_similar_products(self, target_product_id, num_recommendations):
        if target_product_id not in self.product_profiles:
            return []

        target_profile = self.product_profiles[target_product_id]

        # Calcular la similitud del coseno entre el producto objetivo y todos los demás productos
        similarities = []
        for product_id, profile in self.product_profiles.items():
            if product_id != target_product_id:
                similarity = self.cosine_similarity(target_profile, profile)
                similarities.append((product_id, similarity))

        # Ordenar productos por similitud en orden descendente
        similarities.sort(key=lambda x: x[1], reverse=True)

        # Obtener las recomendaciones basadas en similitud
        recommended_products = [product_id for product_id, _ in similarities[:num_recommendations]]

        return recommended_products

# Crear una instancia de ContentBasedRecommendation con los perfiles de productos
product_profiles = {
    product1_id: profile1,
    product2_id: profile2,
    # ...
}
content_recommender = ContentBasedRecommendation(product_profiles)

# Obtener recomendaciones para un producto específico
target_product_id = "target_product_id"
num_recommendations = 5
recommendations = content_recommender.get_similar_products(target_product_id, num_recommendations)

print("Recomendaciones basadas en contenido:", recommendations)