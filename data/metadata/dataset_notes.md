# Dataset Notes

## Project dataset
This project uses BSE SEM images of shale for pore segmentation and porosity estimation.

## Image type
- Backscattered Electron (BSE) Scanning Electron Microscopy (SEM) images
- Grayscale imagery
- Used for identifying pore vs non-pore regions in shale microstructure

## Magnifications used
The dataset includes images at multiple magnifications, including:
- 400x
- 1000x
- 2000x
- 3000x

## Associated outputs
For each selected image, the following files may be generated and stored during the project workflow:
- raw SEM image
- cropped SEM image
- Weka classified result
- pore probability map
- solid probability map
- binary pore mask
- porosity measurement result

## Label source
Initial segmentation labels are produced using Trainable Weka Segmentation in Fiji / ImageJ. These masks are used as reference labels for Python-based machine learning models.

## Planned comparisons
The project will compare:
- Weka segmentation
- Otsu thresholding
- Random Forest classification
- Simple CNN classification

## Purpose of dataset
The dataset is used to evaluate how different segmentation methods affect:
- pore identification
- segmentation quality
- porosity estimates

## Notes
This is a small project dataset prepared for the GEOL0069 AI4EO final assignment. It is intended as a pilot study rather than a large-scale benchmark dataset.
