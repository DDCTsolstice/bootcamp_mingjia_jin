

# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.
## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.
## Data Storage

This project saves data in two structured folders:

project/  
└── data/  
├── raw/ ← snapshot files (.csv)  
└── processed/ ← cleaned files (.parquet)

--- 

Files are timestamped like:

sample_YYYYMMDD-HHMMSS.csv  
sample_YYYYMMDD-HHMMSS.parquet

---

### Data Store Environment Configuration

File paths are defined in `.env`:

env
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=ata/processed

---
---

## Assumptions Made During Data Cleaning

In the cleaning process, we made the following assumptions to ensure consistency, robustness, and reusability of our pipeline:

---

### 1. Missing Value Imputation
- **Assumption:** For all numeric columns, missing values are **not missing completely at random**, and therefore carry some statistical meaning.
- **Action:** We impute missing numeric values using the **median** of each column, which is **robust to outliers** and helps preserve distribution shape.

---

### 2. Column Removal Based on Missing Ratio
- **Assumption:** Columns with more than **50% missing values** are **not trustworthy** and provide little usable information.
- **Action:** We drop any column where more than 50% of the values are missing. This helps reduce noise and dimensionality.

---

### 3. Feature Scaling (Normalization)
- **Assumption:** The dataset may be used for machine learning or statistical models that are **sensitive to feature scale** (e.g., k-NN, regression).
- **Action:** We standardize all numeric features using **z-score normalization** (mean = 0, std = 1) to put them on the same scale.

---

### 4. Date Parsing
- **Assumption:** The `Date` column is essential for time-based operations and must be parsed correctly.
- **Action:** We convert the `Date` column to `datetime` format at load time to ensure temporal operations can be applied properly.

---

### 5. Reproducibility
- **Assumption:** Data pipelines should be repeatable and trackable across time.
- **Action:** We add a **timestamp** to all saved output filenames to ensure version control and easy comparison across runs.

---

These assumptions are based on standard data preprocessing practices and aim to balance data retention, statistical rigor, and pipeline clarity.