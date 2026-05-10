# AI4EO Final Project: SEM Pore Segmentation and Porosity Estimation

## Project overview
This project investigates machine learning approaches for pore segmentation in BSE SEM images of shale. Trainable Weka Segmentation in Fiji is used to generate labelled masks, which are then used as training labels for Python-based machine learning models.

## Background
Quantifying pore space in shale from BSE SEM imagery is important for understanding microstructure and porosity. This project adapts the AI workflow taught in GEOL0069 AI4EO to a geoscience image-analysis problem by comparing classical image processing and supervised machine learning methods.

## Aim
The aim of this project is to compare classical and supervised segmentation methods for pore identification and porosity estimation in SEM images.

## Methods compared
- Trainable Weka Segmentation (Fiji / ImageJ)
- Otsu thresholding
- Random Forest
- Simple Convolutional Neural Network (CNN)

## Research questions
1. Can Weka-labelled SEM masks be used as training labels for Python machine learning models?
2. How do Random Forest and CNN predictions compare with Weka and Otsu thresholding?
3. How do porosity estimates vary between methods?

## Data
The dataset consists of BSE SEM images of shale at multiple magnifications, including:
- 400x
- 1000x
- 2000x
- 3000x

For each selected image, the project may include:
- raw SEM image
- cropped image
- Weka segmentation mask
- probability map
- binary pore mask
- porosity measurement

## Workflow
1. Prepare and organise raw SEM images
2. Generate labelled masks in Fiji using Trainable Weka Segmentation
3. Build a classical baseline using Otsu thresholding
4. Train a Random Forest classifier
5. Train a simple CNN
6. Roll out predictions on full SEM images
7. Compare segmentation quality and porosity estimates between methods

## Repository structure
- `data/` – raw images, cropped images, masks, probability maps, and metadata
- `notebooks/` – notebooks for dataset inspection, baselines, model training, and evaluation
- `src/` – reusable Python scripts
- `figures/` – figures for the final assignment
- `results/` – saved models, prediction outputs, porosity tables, and evaluation results

## Course relevance
This project follows the machine learning workflow taught in GEOL0069 AI4EO: problem definition, data preparation, model development, evaluation, and full-image prediction. Although the course examples focus on Earth Observation imagery, this project applies the same workflow to SEM-based shale pore segmentation.

## Current status
Repository structure created. Weka-based segmentation workflow established for selected SEM images. Python baseline and machine learning implementation in progress.

## Assignment deliverables
This repository supports the final assignment deliverables:
- problem description
- figure illustrating the imaging technique
- diagram of the AI algorithm and implementation
- well-documented GitHub repository with Python code
- video explanation of the workflow

## Author
GEOL0069 AI4EO final project by Courtney Orla Brown.


