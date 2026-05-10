"""
Inference utilities for the GEOL0069 AI4EO SEM segmentation project.

This module is a placeholder for:
- loading trained Random Forest and CNN models
- running predictions on SEM image patches
- rebuilding full-size prediction maps
- saving predicted segmentation outputs
"""

from pathlib import Path
import numpy as np
from joblib import load
from tensorflow.keras.models import load_model


def load_random_forest_model(model_path):
    """
    Load a trained Random Forest model.

    Parameters
    ----------
    model_path : str or Path
        Path to the saved .joblib model file.

    Returns
    -------
    model
        Loaded Random Forest model.
    """
    return load(model_path)


def load_cnn_model(model_path):
    """
    Load a trained CNN model.

    Parameters
    ----------
    model_path : str or Path
        Path to the saved .h5 model file.

    Returns
    -------
    model
        Loaded Keras model.
    """
    return load_model(model_path)


def predict_random_forest(model, X):
    """
    Run inference using a Random Forest model.

    Parameters
    ----------
    model
        Trained Random Forest model.
    X : np.ndarray
        Input feature matrix of shape (n_samples, n_features).

    Returns
    -------
    np.ndarray
        Predicted labels.
    """
    return model.predict(X)


def predict_cnn(model, X, threshold=0.5):
    """
    Run inference using a CNN model.

    Parameters
    ----------
    model
        Trained CNN model.
    X : np.ndarray
        Input array of shape (n_samples, height, width, channels).
    threshold : float
        Decision threshold for binary classification.

    Returns
    -------
    np.ndarray
        Binary predicted labels.
    """
    probabilities = model.predict(X, verbose=0)
    return (probabilities >= threshold).astype(int).ravel()


def rebuild_prediction_map(predictions, image_shape):
    """
    Reshape a flat prediction array back into a 2D map.

    Parameters
    ----------
    predictions : np.ndarray
        Flat array of predictions.
    image_shape : tuple
        Desired 2D output shape, e.g. (rows, cols).

    Returns
    -------
    np.ndarray
        Rebuilt 2D prediction map.
    """
    return np.reshape(predictions, image_shape)


def main():
    """
    Run a small placeholder inference example.
    """
    dummy_predictions = np.random.randint(0, 2, size=100)
    prediction_map = rebuild_prediction_map(dummy_predictions, (10, 10))
    print("Prediction map shape:", prediction_map.shape)


if __name__ == "__main__":
    main()
