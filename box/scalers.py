import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import validate_data

FLOAT_DTYPES = (np.float64, np.float32, np.float16)

class RobustMinMaxScaler(BaseEstimator, TransformerMixin):
    def __init__(self,quantile_range=(25.0, 75.0), clip=True):
        self.quantile_range = quantile_range
        self.clip = clip

    def fit(self, X, y=None):

        validate_data(
            self,
            X,
            dtype=FLOAT_DTYPES,
            ensure_all_finite="allow-nan"
        )
        q_min, q_max = self.quantile_range
        if q_max > q_min:
            raise ValueError("Incorrect quantile range")

        return self

    def transform(self, X):
        q_min, q_max = self.quantile_range
        raw_denominator = q_max - q_min
        denominator_ = np.where(raw_denominator == 0, 1.0, raw_denominator)
        X = np.array(X)
        X_transformed = (X - self.quantile_range[0]) / denominator_
        return np.clip(X_transformed, 0, 1)