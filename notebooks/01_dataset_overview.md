# 01 Dataset Overview

## Purpose
This notebook/page provides an overview of the dataset used in the GEOL0069 AI4EO final project. The project investigates pore segmentation and porosity estimation in BSE SEM images of shale using both classical image processing and supervised machine learning methods. [Source](https://www.genspark.ai/api/files/s/KbhxBNwQ)

## Project context
The project adapts the machine learning workflow taught in GEOL0069 AI4EO to a microstructural geoscience imaging problem. The course emphasizes a standard ML pipeline involving problem definition, data collection, preprocessing, model development, evaluation, and optimisation. This project follows that same structure using SEM imagery instead of satellite Earth Observation imagery. [Source](https://cpomucl.github.io/GEOL0069-AI4EO/Chapter%201%3AML.html)

## Dataset description
The dataset consists of grayscale BSE SEM images of shale collected at multiple magnifications. These images are used to identify pore and non-pore regions and to compare segmentation outputs from different methods. The planned magnifications include:
- 400x
- 1000x
- 2000x
- 3000x

Each selected image may have associated derived outputs such as cropped images, Weka masks, probability maps, binary pore masks, and porosity measurements. [Source](https://www.genspark.ai/api/files/s/KbhxBNwQ)

## Label source
Reference labels for supervised learning are generated using Trainable Weka Segmentation in Fiji / ImageJ. These Weka-derived masks are used as the main label source for Python-based machine learning experiments. This follows the same logic as the course workflow, where manually or interactively generated masks are used as training labels for later AI models. [Source](https://imagej.net/Trainable_Weka_Segmentation) [Source](https://cpomucl.github.io/GEOL0069-AI4EO/Chapter%201%3AIRIS.html)

## Methods to be compared
The project compares four approaches:
- Trainable Weka Segmentation (reference segmentation)
- Otsu thresholding (classical baseline)
- Random Forest
- Simple Convolutional Neural Network (CNN)

This comparison is aligned with the course content, which teaches supervised classification workflows, Random Forest, CNNs, and comparison against simpler baseline methods. [Source](https://cpomucl.github.io/GEOL0069-AI4EO/Chapter_1_AI_Algorithms.html) [Source](https://cpomucl.github.io/GEOL0069-AI4EO/final_assessment.html)

## Expected workflow
The planned workflow for the dataset is:
1. Organise raw SEM images by magnification
2. Crop images where necessary
3. Generate Weka segmentation masks in Fiji
4. Store metadata and porosity values
5. Build an Otsu thresholding baseline
6. Extract image patches for machine learning
7. Train Random Forest and CNN models
8. Roll out predictions on full SEM images
9. Compare segmentation quality and porosity estimates across methods

This structure reflects the course emphasis on end-to-end machine learning workflow and full-image model rollout. [Source](https://cpomucl.github.io/GEOL0069-AI4EO/Chapter%201%3AML.html) [Source](https://cpomucl.github.io/GEOL0069-AI4EO/Chapter_1_rollout_3.html)

## Dataset organisation
The repository stores dataset-related files in the following locations:

- `data/raw/` – raw SEM images
- `data/cropped/` – cropped SEM images
- `data/masks_weka/` – Weka segmentation masks
- `data/probability_maps/` – pore and solid probability maps
- `data/metadata/image_inventory.csv` – image tracking table
- `data/metadata/dataset_notes.md` – dataset notes

## Current status
The repository structure has been created and the dataset tracking files are in progress. Initial Weka-based pore segmentation and porosity measurements have already been produced for selected SEM images, and these will be used to support the baseline and supervised learning stages of the project. [Source](https://www.genspark.ai/api/files/s/v2SBid0z) [Source](https://www.genspark.ai/api/files/s/eJ8Cz4h5)

## Notes
This is a small pilot dataset prepared for the GEOL0069 AI4EO final assignment. It is designed to demonstrate the workflow taught in the module rather than to function as a large-scale benchmark dataset. [Source](https://www.genspark.ai/api/files/s/KbhxBNwQ)
