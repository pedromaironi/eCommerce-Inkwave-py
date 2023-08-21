from product import ProductProfileBasedContent
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.preprocessing import LabelEncoder


class ContentBasedRecommender:
    def __init__(self, product_profiles):
        self.product_profiles = product_profiles
        self.product_features = self._create_product_features()

    def _create_product_features(self):
        product_features = []
        for profile in self.product_profiles:
            product_features.append([
                profile.color,
                profile.price,
            ])
        return product_features

    def _encode_feature(self, feature):
        encoder = LabelEncoder()
        encoded_feature = encoder.fit_transform([feature])
        return encoded_feature[0]

    def recommend_products(self, user_profile):
        user_profile = np.array(user_profile).reshape(1, -1)
        similarity_scores = cosine_similarity(
            user_profile, self.product_features).flatten()
        sorted_indices = np.argsort(similarity_scores)[::-1]
        recommendations = [(self.product_profiles[idx].product_id, similarity_scores[idx])
                           for idx in sorted_indices]
        return recommendations
