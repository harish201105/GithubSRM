# Student Performance Prediction (a model to predict student pass/fail based on the below criteria)

## Project Overview
This project involves developing a machine learning model to predict whether students will pass or fail based on their grades, attendance, homework, and test scores. It uses Python, Pandas, Scikit-learn, and other related libraries to preprocess data, train models, and evaluate their performance.

## Features
- **Grades**: Numeric scores from exams.
- **Attendance**: Percentage of classes attended.
- **Homework**: Numeric scores from homework assignments.
- **Test Scores**: Average test scores before the final exam.
- **Pass/Fail**: Binary outcome indicating pass (1) or fail (0).

## Repository Structure

```
.
├── data
│   └── student_data.csv      # Dataset file
├── notebooks
│   └── model_training.ipynb  # Jupyter notebook for model training
├── src
│   └── datasetgeneration.py  # Python script to generate dataset
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/student-performance-prediction.git
   cd student-performance-prediction
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/model_training.ipynb
   ```

### Usage
To generate a new dataset, run:
```bash
python src/datasetgeneration.py
```
This script will create a new dataset and save it as `data/student_data.csv`, which can be used for training the model in the notebook.

## Model Training and Evaluation
The model training process involves the following steps:
- Data loading and inspection.
- Data preprocessing including scaling and polynomial feature generation.
- Training multiple models using GridSearchCV for hyperparameter tuning.
- Evaluating model performance and selecting the best model.
- Analyzing feature importance to understand the predictors of student success.

For detailed steps and code, refer to the Jupyter Notebook in the `notebooks` directory.

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

