"""
CNN training script for the GEOL0069 AI4EO SEM segmentation project.

This module is a placeholder for:
- loading image patch datasets
- preparing data for CNN input
- defining a simple convolutional neural network
- training the model
- evaluating performance
- saving the trained model
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split


def create_dummy_dataset(n_samples=100, patch_size=9):
    """
    Create a small dummy dataset for testing the CNN pipeline.

    Parameters
    ----------
    n_samples : int
        Number of samples to generate.
    patch_size : int
        Size of square image patches.

    Returns
    -------
    X : np.ndarray
        Dummy feature array of shape (n_samples, patch_size, patch_size, 1).
    y : np.ndarray
        Dummy binary labels of shape (n_samples,).
    """
    X = np.random.rand(n_samples, patch_size, patch_size, 1).astype("float32")
    y = np.random.randint(0, 2, size=n_samples)
    return X, y


def build_simple_cnn(input_shape):
    """
    Build a simple CNN model for binary classification.

    Parameters
    ----------
    input_shape : tuple
        Shape of the input data, e.g. (9, 9, 1).

    Returns
    -------
    tensorflow.keras.Model
        Compiled CNN model.
    """
    model = models.Sequential([
        layers.Input(shape=input_shape),
        layers.Conv2D(16, (3, 3), activation="relu", padding="same"),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(32, (3, 3), activation="relu", padding="same"),
        layers.Flatten(),
        layers.Dense(32, activation="relu"),
        layers.Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
    return model


def main():
    """
    Run a small placeholder CNN training example.
    """
    X, y = create_dummy_dataset()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = build_simple_cnn(input_shape=X_train.shape[1:])

    history = model.fit(
        X_train,
        y_train,
        validation_split=0.2,
        epochs=5,
        batch_size=16,
        verbose=1
    )

    test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"CNN test accuracy: {test_accuracy:.4f}")

    model.save("cnn_placeholder_model.h5")
    print("Saved placeholder model as cnn_placeholder_model.h5")


if __name__ == "__main__":
    main()
