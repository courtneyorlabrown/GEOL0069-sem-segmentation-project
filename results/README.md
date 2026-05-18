# Results

This folder will store project outputs, including:

- trained models
- prediction maps
- porosity tables
- evaluation metrics
- comparison figures

# Final conclusion
This project demonstrates that simple thresholding is not sufficient for pore segmentation in these SEM/BSE images, because it substantially overestimates pore space and performs poorly against the Weka-derived reference masks. Supervised learning methods are more effective for this task, with the Random Forest providing the strongest and most consistent results across the held-out test images.

The CNN offers a useful deep-learning comparison, but on this small dataset it did not clearly outperform the Random Forest. The work therefore highlights both the value and the limits of machine learning in this setting: supervised models can better approximate Weka-style pore segmentation than thresholding alone, but model complexity is not enough on its own when training data are limited and pore space is subtle.

More broadly, the project shows that segmentation strategy directly affects porosity estimates, meaning that image-processing decisions are not just technical details, but part of the geological interpretation itself.




