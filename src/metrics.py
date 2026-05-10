"""
Evaluation metrics for the GEOL0069 AI4EO SEM segmentation project.

This module will contain helper functions for:
- calculating classification metrics
- creating confusion matrices
- summarising model performance
- comparing segmentation outputs
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)


def calculate_metrics(y_true, y_pred):
    """
    Calculate basic classification metrics.

    Parameters
    ----------
    y_true : array-like
        Ground-truth labels.
    y_pred : array-like
        Predicted labels.

    Returns
    -------
    dict
        Dictionary containing accuracy, precision, recall, and F1 score.
    """
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1_score": f1_score(y_true, y_pred, zero_division=0),
    }
    return metrics


def calculate_confusion(y_true, y_pred):
    """
    Calculate the confusion matrix.

    Parameters
    ----------
    y_true : array-like
        Ground-truth labels.
    y_pred : array-like
        Predicted labels.

    Returns
    -------
    np.ndarray
        Confusion matrix.
    """
    return confusion_matrix(y_true, y_pred)


def print_metrics(y_true, y_pred):
    """
    Print evaluation metrics in a readable format.
    """
    metrics = calculate_metrics(y_true, y_pred)
    print("Model performance:")
    for name, value in metrics.items():
        print(f"{name}: {value:.4f}")


def main():
    """
    Run a small placeholder example.
    """
    y_true = [0, 0, 1, 1, 1, 0]
    y_pred = [0, 1, 1, 1, 0, 0]

    print_metrics(y_true, y_pred)
    print("Confusion matrix:")
    print(calculate_confusion(y_true, y_pred))


if __name__ == "__main__":
    main()
