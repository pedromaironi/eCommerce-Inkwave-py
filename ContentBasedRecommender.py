from categories import Categories
from brands import Brands
from sizes import Sizes
from base import DatabaseConnection
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler


class ContentBasedRecommender:
    def __init__(self, product_profiles):
        self.product_profiles = product_profiles
        self.product_features = self._create_product_features()
        self.min_max_scaler = MinMaxScaler()
        self.zscore_scaler = StandardScaler()

    def _create_product_features(self):
        product_features = []

        for profile in self.product_profiles:
            product_features.append([
                profile.color,
                profile.brand,
                profile.size,
                float(profile.price),
                profile.category,
            ])

        return product_features

    def _scale_features(self, features):
        min_max_scaled = self.min_max_scaler.fit_transform(features)
        zscore_normalized = self.zscore_scaler.fit_transform(features)
        return min_max_scaled, zscore_normalized

    def recommend_products(self, user_profile):
        min_max_scaled_features, zscore_normalized_features = self._scale_features(
            self.product_features)

        similarity_scores_minmax = []
        similarity_scores_zscore = []

        for product_feature_minmax, product_feature_zscore in zip(min_max_scaled_features, zscore_normalized_features):
            similarity_minmax = self.calculate_similarity(
                user_profile, product_feature_minmax)
            similarity_scores_minmax.append(similarity_minmax)

            similarity_zscore = self.calculate_similarity(
                user_profile, product_feature_zscore)
            similarity_scores_zscore.append(similarity_zscore)

        print(user_profile.index)
        sorted_indices_minmax = np.argsort(similarity_scores_minmax)[::-1]
        recommendations_minmax = [(self.product_profiles[idx].product_id, similarity_scores_minmax[idx])
                                  for idx in sorted_indices_minmax
                                  if self.product_profiles[idx].category == user_profile[4]
                                  or self.product_profiles[idx].brand == user_profile[1]]

        sorted_indices_zscore = np.argsort(similarity_scores_zscore)[::-1]
        recommendations_zscore = [(self.product_profiles[idx].product_id, similarity_scores_zscore[idx])
                                  for idx in sorted_indices_zscore
                                  if self.product_profiles[idx].category == user_profile[4]
                                  or self.product_profiles[idx].brand == user_profile[1]]

        return recommendations_minmax, recommendations_zscore

    def calculate_similarity(self, user_profile, product_feature):
        user_profile_array = np.array(user_profile).reshape(1, -1)
        product_feature_array = np.array(product_feature).reshape(1, -1)

        similarity = cosine_similarity(
            user_profile_array, product_feature_array)[0][0]
        return similarity

    def calculate_similarity_matrix(self, user_profile):
        similarity_matrix = []

        for product_feature in self.product_features:
            similarity = self.calculate_similarity(
                user_profile, product_feature)
            similarity_matrix.append(similarity)

        return similarity_matrix
