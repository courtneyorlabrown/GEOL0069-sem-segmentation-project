"""
Otsu thresholding baseline for the GEOL0069 AI4EO SEM segmentation project.

This module is a placeholder for:
- loading grayscale SEM images
- applying Otsu thresholding
- generating binary pore masks
- calculating simple pore fractions
"""

from pathlib import Path
import numpy as np
from skimage.filters import threshold_otsu


def apply_otsu_threshold(image):
    """
    Apply Otsu thresholding to a grayscale image.

    Parameters
    ----------
    image : np.ndarray
        Input 2D grayscale image.

    Returns
    -------
    binary_mask : np.ndarray
        Binary mask produced using Otsu thresholding.
    threshold_value : float
        Threshold selected by Otsu's method.
    """
    threshold_value = threshold_otsu(image)
    binary_mask = image > threshold_value
    return binary_mask.astype(np.uint8), threshold_value


def calculate_porosity(binary_mask):
    """
    Calculate pore fraction from a binary mask.

    Parameters
    ----------
    binary_mask : np.ndarray
        Binary image where pore pixels are 1 and non-pore pixels are 0.

    Returns
    -------
    float
        Porosity as a fraction of image area.
    """
    return float(np.mean(binary_mask))


def main():
    """
    Run a small placeholder Otsu example.
    """
    dummy_image = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)

    binary_mask, threshold_value = apply_otsu_threshold(dummy_image)
    porosity = calculate_porosity(binary_mask)

    print(f"Otsu threshold value: {threshold_value:.2f}")
    print(f"Estimated porosity: {porosity:.4f}")
    print("Binary mask shape:", binary_mask.shape)


if __name__ == "__main__":
    main()
