# Heart Disease Exploratory Data Analysis

## Project Overview

This project analyzes a clinical heart disease dataset to identify patient patterns, data quality issues, numeric risk signals, categorical disease indicators, and probability-based risk differences. The goal is not only to create charts, but to build a structured end-to-end exploratory data analysis workflow that explains **who is represented in the dataset**, **which features separate sick and healthy patients**, and **which clinical indicators may signal higher heart disease risk**.

The analysis uses Python, pandas, NumPy, Matplotlib, Seaborn, and a reusable custom Python class to make the notebook cleaner and easier to maintain.

## Dataset Summary

The dataset contains patient-level heart disease information with clinical and diagnostic features.

The target column is:

* `HeartDisease = 0`: patient does not have heart disease
* `HeartDisease = 1`: patient has heart disease

The dataset includes features such as:

* Age
* Sex
* ChestPainType
* RestingBP
* Cholesterol
* FastingBS
* RestingECG
* MaxHR
* ExerciseAngina
* Oldpeak
* ST_Slope
* HeartDisease

The raw CSV file is stored locally inside the `data/` folder and should not be pushed to GitHub.

## Business / Clinical Questions

This project answers five main questions:

### 1. Who is represented in this dataset?

I explored patient age range, gender distribution, and heart disease balance to understand the population represented in the data.

### 2. Which numeric features separate sick and healthy patients?

I compared numeric features such as `Age`, `MaxHR`, `Oldpeak`, `RestingBP`, and `Cholesterol` using boxplots, group means, and a correlation heatmap.

### 3. Which categorical features show the highest disease rates?

I calculated disease rates across categories such as `ChestPainType`, `ExerciseAngina`, and `ST_Slope` to identify high-risk symptom groups.

### 4. How does probability change when exercise-induced angina is present?

I calculated prior probability, conditional probability, and verified the result using Bayes theorem.

### 5. Does ST slope remain important across age groups?

I grouped patients into age bands and compared disease rates across `ST_Slope` categories to see whether ST slope remains a strong risk signal after accounting for age.

## Key Insights

1. The dataset contains **917 patients**, with heart disease present in **507 patients (55.3%)** and absent in **410 patients (44.7%)**, making the target variable fairly balanced.

2. The dataset is strongly male-heavy, with **724 male patients (79.0%)** and **193 female patients (21.0%)**, which means the findings may not generalize equally to female patients.

3. The strongest numeric separators are **MaxHR**, **Oldpeak**, and **Age**. Diseased patients average about **20.5 bpm lower MaxHR**, **0.86 higher Oldpeak**, and **5.3 years older** than healthy patients.

4. Categorical symptoms show strong disease-rate differences. Patients with **ExerciseAngina = Y** have about an **85%** heart disease rate, compared with about **35%** for patients with ExerciseAngina = N.

5. The dirty-data investigation found that **zero Cholesterol values were not safe to drop** because that group had about an **88.4% disease rate**. Dropping those rows would remove many diseased patients and bias the dataset toward healthier cases.

## Dirty-Data Discovery

A major part of this analysis was identifying disguised missing values.

The dataset showed zero values in:

* `Cholesterol`
* `RestingBP`

These zero values are biologically unrealistic for living patients, so they were treated as likely missing or incorrectly recorded values.

The zero-Cholesterol group was especially important because patients with zero Cholesterol had a very high heart disease rate of about **88.4%**. Dropping these rows would remove many diseased patients and distort the dataset. Because Cholesterol also contained outliers, median imputation was selected as a safer cleaning strategy than mean imputation.

## Visualizations

### Age Distribution
![Age Distribution](images/01_age_distribution.png)

### Gender Ratio
![Gender Ratio](images/02_gender_ratio.png)

### Disease Ratio
![Disease Ratio](images/03_disease_ratio.png)

### Numeric Boxplots
![Numeric Boxplots](images/04_numeric_boxplots.png)

### Correlation Heatmap
![Correlation Heatmap](images/05_correlation_heatmap.png)

### Chest Pain Disease Rate
![Chest Pain Disease Rate](images/06_chestpain_disease_rate.png)

### Exercise Angina Disease Rate
![Exercise Angina Disease Rate](images/07_exercise_angina_disease_rate.png)

### ST Slope Disease Rate
![ST Slope Disease Rate](images/08_st_slope_disease_rate.png)

### Age Group and ST Slope
![Age Group and ST Slope](images/09_age_group_st_slope.png)

## Methods Used

This project uses:

* Data loading and inspection
* Summary statistics
* Value counts for categorical columns
* Dirty-data detection
* Missing-value strategy
* Median imputation
* Grouped aggregation
* Disease-rate calculations
* Conditional probability
* Bayes theorem verification
* Histogram, count plot, boxplot, bar chart, heatmap, and catplot visualizations
* Reusable Python class design

## Reusable Python Class

The project includes a reusable `DataExplorer` class inside `src/explorer.py`.

This class helps reduce repeated notebook code and makes the project more structured.

Main methods include:

* `shape()`: returns dataset shape
* `preview()`: previews the first rows
* `null_report()`: checks missing values
* `zero_report()`: checks suspicious zero values
* `disease_rate_by()`: calculates disease rate by category
* `cond_prob()`: calculates conditional probability
* `prior_prob()`: calculates baseline disease probability
* `bayes_verify()`: verifies Bayes theorem
* `add_age_group()`: creates age groups
* `rate_by_two_groups()`: calculates disease rate across two grouped variables

## Project Structure

```text
01-heart-disease-eda/
│
├── data/
│   └── heart.csv                  # local dataset only, not pushed to GitHub
│
├── notebooks/
│   └── heart_disease_eda.ipynb
│
├── src/
│   └── explorer.py
│
├── images/
│   ├── 01_age_distribution.png
│   ├── 02_gender_ratio.png
│   ├── 03_disease_ratio.png
│   ├── 04_numeric_boxplots.png
│   ├── 05_correlation_heatmap.png
│   ├── 06_chestpain_disease_rate.png
│   ├── 07_exercise_angina_disease_rate.png
│   ├── 08_st_slope_disease_rate.png
│   └── 09_age_group_st_slope.png
│
├── README.md
├── .gitignore
└── requirements.txt
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd 01-heart-disease-eda
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add the dataset locally

Place the dataset in the `data/` folder:

```text
data/heart.csv
```

### 6. Open and run the notebook

Open the notebook in VS Code or Jupyter Notebook:

```text
notebooks/heart_disease_eda.ipynb
```

Run all cells from top to bottom.

## Requirements

```text
pandas
numpy
matplotlib
seaborn
jupyter
```

## GitHub Notes

The raw dataset should not be pushed to GitHub. The `.gitignore` file should include:

```text
data/
*.csv
__pycache__/
.ipynb_checkpoints/
venv/
.venv/
```

Before pushing to GitHub, verify that the CSV file is not tracked:

```bash
git ls-files
```

The repository should include:

* Notebook
* README
* Source code
* Chart images
* `.gitignore`
* `requirements.txt`

The repository should not include:

* Raw CSV dataset
* Virtual environment folder
* Cache files
* Notebook checkpoint files

## Final Conclusion

This analysis shows that heart disease risk is strongly associated with lower maximum heart rate, higher ST depression, older age, exercise-induced angina, asymptomatic chest pain, and abnormal ST slope patterns. The project also highlights the importance of data quality checks, because the zero-Cholesterol records looked invalid but represented a highly diseased group that should not be dropped blindly.

Overall, this project demonstrates a complete exploratory data analysis workflow: understanding the dataset, identifying dirty data, generating visual evidence, calculating probabilities, and organizing reusable analysis code.
