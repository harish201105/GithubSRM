import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Define the number of samples
n_samples = 500

# Generate synthetic data
data = pd.DataFrame({
    'Grades': np.random.randint(20, 100, n_samples),        # Random grades between 20 and 100
    'Attendance': np.random.randint(50, 101, n_samples),    # Random attendance percentage between 50% and 100%
    'Homework': np.random.randint(0, 100, n_samples),       # Random homework scores between 0 and 100
    'Test_Scores': np.random.randint(20, 100, n_samples)    # Random test scores between 20 and 100
})

# A simple rule to decide if a student passes or fails
# Example rule: pass if the average score (weighted) + 0.5 * attendance is greater than 120
data['Pass_Fail'] = (0.3 * data['Grades'] + 0.2 * data['Homework'] + 0.5 * data['Test_Scores'] + 0.5 * data['Attendance']).apply(lambda x: 1 if x > 120 else 0)

# Save to CSV
data.to_csv('student_data.csv', index=False)

# Print the first few rows to verify
print(data.head())
