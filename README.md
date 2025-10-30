# Master Thesis: Evaluating and Refining Recommendation Quality: A Case Study of the RecSys Challenge 2024 Winner
# Author: Alana Zoloeva
This project investigates lightweight approaches for personalized news recommendation in the context of the **RecSys Challenge 2024**, focusing on **cold-start users** and **model interpretability**.
The main objective was to improve **AUC** and beyond-accuracy metrics (diversity, novelty) while maintaining minimal model complexity.

The code used to create the model for my thesis is in the following notebook: **./thesis.ipynb**
To run the model of winners of the challenge, follow instructions in **./README_winners.md**

## Methodology

The proposed pipeline consists of three key components:

1. **Feature Engineering:** Constructed user, article, and contextual features, including clustering-based personalization for users with ≤7 clicks.
2. **Learning-to-Rank Models:** Evaluated **CatBoost** and **LightGBM** as interpretable, resource-efficient alternatives to transformer-based rerankers.
3. **Hyperparameter Optimization:** Applied **Optuna** for efficient parameter tuning with cross-validation and early stopping.

## Results and Insights

Despite using the smaller dataset version due to hardware constraints, the **CatBoost** model achieved strong **AUC** and **MRR** performance, outperforming tree-based baselines while remaining computationally lightweight.
Clustering cold-start users improved AUC, confirming that even coarse segmentation enhances personalization under sparse data.

## Conclusion

This work demonstrates that interpretable gradient-boosting models with targeted cold-start strategies can achieve robust performance in news recommendation tasks, offering a practical, explainable alternative to complex deep-learning architectures in production settings.

