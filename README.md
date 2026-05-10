# AI4EO Final Project: SEM Pore Segmentation and Porosity Estimation

## Project overview
This project investigates machine learning approaches for pore segmentation in BSE SEM images of shale. 
Trainable Weka Segmentation in Fiji is used to generate labelled masks, which are then used as training labels for Python-based machine learning models.

## Aim
To compare classical and supervised segmentation methods for pore identification and porosity estimation:
- Weka segmentation
- Otsu thresholding
- Random Forest
- Simple CNN

## Research questions
1. Can Weka-labelled SEM masks be used as training labels for Python ML models?
2. How do Random Forest and CNN predictions compare with Weka and Otsu?
3. How do porosity estimates vary between methods?

## Data
The dataset consists of BSE SEM images of shale at multiple magnifications.

## Planned workflow
1. Prepare raw SEM images
2. Generate labelled masks in Fiji using Trainable Weka Segmentation
3. Build a classical baseline using Otsu thresholding
4. Train a Random Forest model
5. Train a simple CNN
6. Roll out predictions on full SEM images
7. Compare segmentation quality and porosity estimates

## Repository structure
- data/
- notebooks/
- src/
- figures/
- results/

## Status
Project in progress for GEOL0069 AI4EO final assignment.

