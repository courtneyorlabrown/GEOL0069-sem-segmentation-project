# AI4EO Final Project: SEM Pore Segmentation and Porosity Estimation

## Project overview
This repository contains my final project for **GEOL0069: AI for Earth Observation**, focused on **pore-space segmentation and porosity estimation from BSE SEM images** using both classical image-processing and supervised machine-learning approaches. The project is closely aligned with my dissertation work on the **microstructural characterisation of shale and related tight samples**, where pore space is quantified from electron microscopy imagery using **ImageJ / Fiji** and **Trainable Weka Segmentation**.

In this project, **Trainable Weka Segmentation** is used to generate labelled pore masks in Fiji, and these masks are then used as **reference labels** for Python-based machine-learning models. The core objective is to test whether simple machine-learning methods trained from Weka-derived labels can reproduce pore segmentation more reliably than a classical unsupervised thresholding approach, and to examine how **segmentation choice affects derived porosity values**.

---

## Background
Quantifying pore space from **BSE SEM imagery** is important for understanding the microstructure and porosity of shale and other tight geological materials. However, pore-space segmentation in SEM/BSE images is difficult because pores are often **small, sparse, subtle, and visually similar to other dark microstructural features**. This means that simple grey-value thresholding may not be sufficient, especially when pore boundaries are gradual or when other dark phases are present.

This project adapts the **AI workflow taught in GEOL0069 AI4EO** to a geoscience image-analysis problem. Although the course examples focus mainly on Earth Observation imagery, the same workflow can be applied here: define the problem, prepare labelled data, train models, evaluate predictions, and compare full-image outputs. The project therefore provides a direct bridge between the course content and a real dissertation-related microstructural analysis problem.

---

## Aim
The aim of this project is to compare **classical** and **supervised** segmentation methods for **pore identification** and **porosity estimation** in SEM images, using Weka-derived masks as the reference segmentation.

More specifically, the project asks whether Python-based machine-learning models can reproduce Weka-style pore segmentation more effectively than a classical thresholding baseline, and how strongly the choice of segmentation method influences the resulting porosity measurements.

---

## Methods compared
This project compares four related approaches:

- **Trainable Weka Segmentation (Fiji / ImageJ)**  
  Used to create the reference pore masks for the selected SEM images. These masks are treated as the labelled segmentation standard in the project workflow.

- **Otsu thresholding**  
  A classical unsupervised image-processing baseline based on grey-value thresholding.

- **Random Forest**  
  A supervised feature-based machine-learning classifier trained using Weka-derived pore labels.

- **Simple Convolutional Neural Network (CNN)**  
  A patch-based deep-learning model trained to predict pore versus non-pore regions from labelled image patches.

---

## Research questions
This project is structured around the following questions:

1. **Can Weka-labelled SEM masks be used as training labels for Python machine-learning models?**
2. **How do Random Forest and CNN predictions compare with Weka segmentation and with Otsu thresholding?**
3. **How strongly do porosity estimates vary between methods?**
4. **Does a simple CNN outperform a Random Forest on this small SEM/BSE dataset?**

---

## Data
The dataset consists of **BSE SEM images** collected at multiple magnifications, including:

- **400×**
- **1000×**
- **2000×**
- **3000×**

For each selected image, the project may include:

- raw SEM image
- cropped image
- Weka segmentation mask
- probability map
- binary pore mask
- porosity measurement

The workflow uses a small number of carefully selected images in order to build an interpretable proof-of-concept comparison between methods.

---

## Workflow
The project follows a structured workflow:

1. **Prepare and organise raw SEM images**
2. **Generate labelled masks in Fiji using Trainable Weka Segmentation**
3. **Build a classical baseline using Otsu thresholding**
4. **Train a Random Forest classifier**
5. **Train a simple CNN**
6. **Roll out predictions on full SEM images**
7. **Compare segmentation quality and porosity estimates between methods**
8. **Evaluate performance using shared test images and summary metrics**

This allows all methods to be compared on the **same held-out test set**, both qualitatively and quantitatively.

---

## Why Weka is used as the reference
Trainable Weka Segmentation is not treated here as just another competing prediction model. Instead, it provides the **reference segmentation masks** used to train and evaluate the Python-based models.

This is important because Weka can incorporate **expert-guided training** and a wider range of image features than simple thresholding alone. In SEM/BSE pore segmentation, pore space is often not separable from the surrounding matrix by grey value alone. A Weka-based workflow can therefore capture subtler pore boundaries and contextual differences than a global threshold, making it a more suitable reference for this task.

---

## Evaluation metrics
The methods are compared using both **segmentation metrics** and **derived porosity values**.

### Segmentation metrics
- **IoU (Intersection over Union)** — overlap between predicted and reference pore masks
- **Precision** — fraction of predicted pore pixels that are correct
- **Recall** — fraction of true pore pixels successfully recovered
- **F1 score** — harmonic mean of precision and recall, useful when pore pixels are sparse relative to the background

### Quantitative pore metric
- **Porosity (%)** — calculated from the binary pore masks and compared across methods

Together, these metrics allow the project to assess not only whether a method produces visually plausible masks, but also whether it gives **realistic quantitative porosity estimates**.

---

## Main findings
The results show a clear difference in behaviour between the methods.

- **Otsu thresholding performed worst overall**, strongly overestimating porosity and producing poor overlap with the Weka reference masks.
- **Random Forest gave the strongest and most consistent overall performance**, with the best average segmentation metrics on the held-out test images.
- **The CNN provided a useful deep-learning comparison**, and performed reasonably on the higher-porosity images, but it did **not clearly outperform the Random Forest** on this small dataset.
- The project also shows that **segmentation choice has a strong effect on derived porosity values**, even when all methods are applied to the same images.

Overall, the results suggest that **supervised learning is more suitable than simple global thresholding for this task**, but also that **greater model complexity does not automatically lead to better performance** when the dataset is small and the pore signal is weak.

---

## Example results

### Method-level comparison
The figure below summarises the mean performance of the three Python-based methods on the held-out test set. Otsu has by far the largest porosity error, while the Random Forest gives the strongest mean IoU and F1 performance.

![Method comparison summary](figures/comparison_method_summary.png)

### Predicted vs reference porosity
The scatter plots below compare each method’s predicted porosity against the Weka-derived reference porosity. Otsu consistently overestimates pore space, while the Random Forest and CNN remain much closer to the expected values.

![Predicted vs Weka porosity](figures/comparison_scatter_porosity.png)

### Porosity and F1 score by test image
The figure below shows how predicted porosity and F1 score vary for each held-out test image. This highlights the poor behaviour of Otsu, the stronger consistency of the Random Forest, and the more mixed performance of the CNN.

![Porosity and F1 by test image](figures/comparison_by_image.png)

### Qualitative comparison
Visual comparison of the segmentation masks shows the same overall pattern: Otsu tends to classify too much dark material as pore space, whereas the Random Forest and CNN produce masks that are more similar to the Weka-derived reference.

![Qualitative comparison examples](figures/comparison_full_rollout_page_1.png)

---

## Notebook guide
The project is organised into five main notebooks:

### `01_data_loading_and_inventory.ipynb`
Loads the dataset, organises file paths, checks image and mask availability, and creates a structured inventory for the rest of the workflow.

### `02_otsu_baseline.ipynb`
Applies Otsu thresholding as a classical unsupervised baseline and compares predicted pore masks against the Weka reference masks.

### `03_random_forest.ipynb`
Trains a Random Forest classifier using Weka-derived labels and evaluates full-image predictions on the held-out test images.

### `04_cnn_patch_classifier.ipynb`
Trains a patch-based CNN and rolls out predictions across full test images for comparison with Weka and the Random Forest.

### `05_evaluation_and_comparison.ipynb`
Brings all methods together and compares segmentation masks, porosity values, and evaluation metrics on the same held-out test images.

---

## Repository structure
- `data/` – raw images, cropped images, masks, probability maps, and metadata
- `notebooks/` – notebooks for dataset inspection, baselines, model training, and evaluation
- `src/` – reusable Python scripts
- `figures/` – figures for the final assignment and repository documentation
- `results/` – saved models, prediction outputs, porosity tables, and evaluation results

A simplified project tree is shown below:

```text
GEOL0069-sem-segmentation-project/
├── notebooks/
│   ├── 01_data_loading_and_inventory.ipynb
│   ├── 02_otsu_baseline.ipynb
│   ├── 03_random_forest.ipynb
│   ├── 04_cnn_patch_classifier.ipynb
│   └── 05_evaluation_and_comparison.ipynb
├── data/
│   ├── cropped/
│   ├── masks_weka/
│   ├── metadata/
│   ├── probability_maps/
│   └── raw/
├── figures/
├── results/
├── src/
├── requirements.txt
└── README.md

Author:
Courtney Orla Brown
GEOL0069 AI4EO final project
