# Week 5 Task 1: Introduction to Machine Learning & Linear Regression

This directory contains the implementation for Week 5 Task 1 of the AI/ML Fellowship. The goal is to understand the basics of Machine Learning and implement Linear Regression.

## Contents

- **`Week 5 task 1.ipynb`**: A Jupyter Notebook containing:
  1. **Introduction**: Brief overview of Machine Learning and Linear Regression.
  2. **Data Generation**: Code to generate a synthetic dataset with a linear relationship and Gaussian noise.
  3. **From Scratch Implementation**: Custom Python implementation of Gradient Descent to optimize the Mean Squared Error cost function. Finds the optimal slope and intercept without relying on external ML libraries.
  4. **Scikit-Learn Implementation**: Validation of the custom algorithm using `sklearn.linear_model.LinearRegression`.

## Technologies Used

- Python 3
- NumPy
- Matplotlib
- Scikit-Learn
- Jupyter Notebook

## How to Run

1. Ensure you have a Python virtual environment set up with the required dependencies (refer to the root `requirements.txt` or install them manually: `pip install numpy matplotlib scikit-learn jupyter`).
2. Navigate to this directory.
3. Launch Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

4. Open `Week 5 task 1.ipynb` and run the cells.
