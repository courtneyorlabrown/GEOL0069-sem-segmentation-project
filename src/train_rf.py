"""
Random Forest training script for the GEOL0069 AI4EO SEM segmentation project.

This module is a placeholder for:
- loading training data
- reshaping patch data for Random Forest input
- training a Random Forest classifier
- saving the trained model
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump


def create_dummy_dataset(n_samples=100, patch_size=9):
    """
    Create a small dummy dataset for testing the training pipeline.

    Parameters
    ----------
    n_samples : int
        Number of samples to generate.
    patch_size : int
        Size of square image patches.

    Returns
    -------
    X : np.ndarray
        Dummy feature array of shape (n_samples, patch_size, patch_size).
    y : np.ndarray
        Dummy binary labels of shape (n_samples,).
    """
    X = np.random.rand(n_samples, patch_size, patch_size)
    y = np.random.randint(0, 2, size=n_samples)
    return X, y


def reshape_for_random_forest(X):
    """
    Reshape patch data into 2D format for scikit-learn Random Forest.

    Parameters
    ----------
    X : np.ndarray
        Input patch array of shape (n_samples, height, width).

    Returns
    -------
    np.ndarray
        Reshaped array of shape (n_samples, height * width).
    """
    return X.reshape(X.shape[0], -1)


def train_random_forest(X, y, n_estimators=100, random_state=42):
    """
    Train a Random Forest classifier.

    Parameters
    ----------
    X : np.ndarray
        Feature array.
    y : np.ndarray
        Label array.
    n_estimators : int
        Number of trees in the forest.
    random_state : int
        Random seed for reproducibility.

    Returns
    -------
    model : RandomForestClassifier
        Trained Random Forest model.
    """
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state
    )
    model.fit(X, y)
    return model


def main():
    """
    Run a small placeholder training example.
    """
    X, y = create_dummy_dataset()
    X = reshape_for_random_forest(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = train_random_forest(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"Random Forest test accuracy: {accuracy:.4f}")

    dump(model, "random_forest_placeholder.joblib")
    print("Saved placeholder model as random_forest_placeholder.joblib")


if __name__ == "__main__":
    main()
