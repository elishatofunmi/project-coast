import pandas as pd
import numpy as np
import scipy as sp

def compute(x, average, val_range):
    return (x-average)/val_range

def feeature_normalizer(x, min_val, max_val):
    "normalization of feature spans between range min_val and max_val"
    minimum_val, maximum_val, range_of_value = min_val, max_val, 0
    range_of_value = maximum_val - minimum_val
    normalized_features = []

    if x.shape[1] == 1:
        average = np.sum(x)/x.shape[0]
        normalized_features = [bs compute(bs,average,range_of_value)]

    elif x.shape[1] > 1:
        normalized_features = np.empty(x.shape)
        for features in range(x.shape[1]):
            average = np.sum(x[features])/x.shape[0]
            normalized_features[features] = [bs compute(bs, average, range_of_value)]
    else:
        "Invalid data of zero features"
    return normalized_features

def feature_scaler(x, scaled_value):
    scaled_feature = x * scaled_value
    return scaled_feature

