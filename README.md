# Football Match Outcome Prediction Using Machine Learning

## 📘 Project Overview

This project applies machine learning classification techniques to predict international football match outcomes (Win, Draw, or Loss) based on historical match data. The models implemented include Logistic Regression and Gradient Boosting, both evaluated with multiple performance metrics.

## 🎯 Objectives

- Build a classification model to predict match outcomes
- Understand the impact of pre-match factors on prediction
- Compare baseline (Logistic Regression) and advanced (Gradient Boosting) models

## 📂 Dataset

- Source: Open dataset covering international men's matches (1872–2025)
- Observations: 48,208 matches
- Features: Teams, tournament type, neutral venue, year, and engineered features

## 🛠️ Features Used

- `home_team`, `away_team`, `tournament`
- `home_advantage`: binary indicator for neutral venue
- `year`: extracted from date
- `is_final`, `is_friendly`: binary tournament context features

## 🧪 Models Implemented

- **Logistic Regression**: Multinomial, serves as a linear baseline
- **Gradient Boosting Classifier**: Non-linear, more powerful for tabular data

## 🔍 Evaluation Metrics

- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix
- ROC & Precision-Recall Curves
- Cross-validation (5-fold)

## 💡 Key Insights

- Gradient Boosting outperformed Logistic Regression (~59% vs. ~53% accuracy)
- Feature engineering (tournament type, venue, year) improved performance
- ROC and PR curves highlighted class separation quality

## ⚙️ Tech Stack

- Python 3.10
- Libraries: Pandas, Scikit-learn, Matplotlib, Seaborn, XGBoost, Imbalanced-learn

## 💻 Getting Started

1. Clone this repository
2. Install dependencies from `requirements.txt`
3. Run `notebook.ipynb` in Jupyter

## 📈 Future Work

- Integrate FIFA rankings
- Explore deep learning (LSTMs)
- Add player/team performance stats
"""

# Save to file
readme_path = "/mnt/data/README.md"
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

readme_path

## References
UCI Machine Learning Repository (2019) Apartment for Rent Classified. [online] Available at: https://doi.org/10.24432/C5X623 [Accessed 3 Apr. 2025].

YouTube (2025) Download Kaggle Datasets via API in Python. [video] Available at: https://youtu.be/hzcV0hDkfzs [Accessed 3 Apr. 2025].

YouTube (2023) How to Install Git & Use Git in Visual Studio Code. [video] Available at: https://youtu.be/3Tsaxxv9sls [Accessed 3 Apr. 2025].

YouTube (2023) How to Use Git in Visual Studio Code. [video] Available at: https://youtu.be/z5jZ9lrSpqk [Accessed 3 Apr. 2025].

YouTube (2025) How to Find and Use Kaggle Datasets in Your Project. [video] Available at: https://youtu.be/krkS9u140tM [Accessed 3 Apr. 2025].

YouTube (2020) How to Download Kaggle Datasets using the Kaggle API. [video] Available at: https://youtu.be/gkEbaMgvLs8 [Accessed 3 Apr. 2025].
