# Mental Health ML Project

## Overview

This project explores a mental health dataset using data analysis and machine learning techniques.
The goal is to understand patterns in the data and build models that can help predict mental health conditions.

## Project Structure

```
Mental-health-ml-project
│
├── data/
│   └── mental_health_dataset.csv
│
├── notebooks/
│   └── mental_health_analysis.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   └── models.py
│
├── requirements.txt
└── README.md
```

## Features

* Data loading utilities
* Data preprocessing pipeline
* Exploratory data analysis
* Machine learning model experiments

## Results

The following models were trained and evaluated:

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 0.52 |
| Decision Tree | 0.47 |
| Random Forest | 0.55 |

Random Forest acheived the best perfomance among the tested models.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

## Installation

Clone the repository and install dependencies:

```
git clone <repo-url>
cd Mental-health-ml-project
pip install -r requirements.txt
```

## Running the Analysis

Start Jupyter Notebook and open the analysis file:

```
jupyter notebook notebooks/mental_health_analysis.ipynb
```