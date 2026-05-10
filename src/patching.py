"""
Patch extraction utilities for the GEOL0069 AI4EO SEM segmentation project.

This module will contain helper functions for:
- defining patch sizes
- extracting square image patches around a pixel
- preparing patch datasets for Random Forest and CNN models
- checking patch dimensions
"""

import numpy as np


def describe_patching():
    """Print a short description of this patching module."""
    print("Patch extraction module for SEM segmentation.")


def extract_patch(image, center_row, center_col, patch_size=9):
    """
    Extract a square patch from a 2D image around a central pixel.

    Parameters
    ----------
    image : np.ndarray
        Input 2D grayscale image.
    center_row : int
        Row index of the patch center.
    center_col : int
        Column index of the patch center.
    patch_size : int
        Size of the square patch. Must be an odd number.

    Returns
    -------
    np.ndarray
        Extracted image patch.
    """
    if patch_size % 2 == 0:
        raise ValueError("patch_size must be an odd number.")

    half = patch_size // 2

    row_start = center_row - half
    row_end = center_row + half + 1
    col_start = center_col - half
    col_end = center_col + half + 1

    return image[row_start:row_end, col_start:col_end]


def main():
    """Run a simple placeholder example."""
    example_image = np.zeros((20, 20))
    patch = extract_patch(example_image, center_row=10, center_col=10, patch_size=9)
    print("Extracted patch shape:", patch.shape)


if __name__ == "__main__":
    main()
