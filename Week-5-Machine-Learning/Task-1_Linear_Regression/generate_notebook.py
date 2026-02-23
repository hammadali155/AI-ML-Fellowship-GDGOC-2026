import nbformat as nbf
import subprocess
import os
import time

NOTEBOOK_NAME = "Week 5 task 1.ipynb"
COMMIT_DELAY = 2  # giving git time to process

def run_git_command(command, commit_msg=None):
    try:
        if commit_msg:
            # Add specific file
            subprocess.run(["git", "add", NOTEBOOK_NAME], check=True)
            # Commit
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            print(f"Committed: {commit_msg}")
        else:
            subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")

def create_initial_notebook():
    nb = nbf.v4.new_notebook()
    # Stage 1: Setup and Introduction
    nb['cells'] = [
        nbf.v4.new_markdown_cell("# Week 5 Task 1: Introduction to Machine Learning & Linear Regression\n\nThis notebook demonstrates the implementation of Linear Regression both from scratch using Gradient Descent and using the `scikit-learn` library."),
        nbf.v4.new_markdown_cell("## 1. Introduction to Machine Learning\n\nMachine Learning is a field of study that gives computers the ability to learn without being explicitly programmed. In supervised learning (like Linear Regression), algorithms learn from labeled training data to make predictions on unseen data."),
        nbf.v4.new_code_cell("import numpy as np\nimport matplotlib.pyplot as plt\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import mean_squared_error\n\n# Configure matplotlib for consistent plotting\n%matplotlib inline\nplt.style.use('seaborn-v0_8-darkgrid')")
    ]
    with open(NOTEBOOK_NAME, 'w') as f:
        nbf.write(nb, f)
    print("Stage 1 complete.")
    run_git_command(None, "Add Introduction and Library Imports for Week 5 Task 1")
    time.sleep(COMMIT_DELAY)

def add_data_generation():
    with open(NOTEBOOK_NAME, 'r') as f:
        nb = nbf.read(f, as_version=4)
        
    nb['cells'].extend([
        nbf.v4.new_markdown_cell("## 2. Data Generation and Preprocessing\n\nWe will generate a synthetic dataset with a linear relationship: $y = 3X + 4 + noise$."),
        nbf.v4.new_code_cell("# Set random seed for reproducibility\nnp.random.seed(42)\n\n# Generate 100 random points for X between 0 and 2\nX = 2 * np.random.rand(100, 1)\n\n# Generate y with the true linear relationship y = 4 + 3x0 plus some Gaussian noise\ny = 4 + 3 * X + np.random.randn(100, 1)\n\n# Visualize the generated dataset\nplt.figure(figsize=(8, 5))\nplt.scatter(X, y, color='blue', alpha=0.6, label='Data points')\nplt.xlabel('X (Feature)')\nplt.ylabel('y (Target)')\nplt.title('Synthetic Data for Linear Regression')\nplt.legend()\nplt.show()")
    ])
    
    with open(NOTEBOOK_NAME, 'w') as f:
        nbf.write(nb, f)
    print("Stage 2 complete.")
    run_git_command(None, "Add synthetic data generation and visualization")
    time.sleep(COMMIT_DELAY)

def add_linear_regression_scratch():
    with open(NOTEBOOK_NAME, 'r') as f:
        nb = nbf.read(f, as_version=4)
        
    nb['cells'].extend([
        nbf.v4.new_markdown_cell("## 3. Linear Regression from Scratch using Gradient Descent\n\nIn this section, we implement the Gradient Descent algorithm to minimize the Cost Function (Mean Squared Error) and find the optimal parameters $\\theta_0$ (intercept) and $\\theta_1$ (slope)."),
        nbf.v4.new_markdown_cell("### Cost Function (Mean Squared Error)\n$J(\\theta) = \\frac{1}{2m} \sum_{i=1}^{m} (h_\\theta(x^{(i)}) - y^{(i)})^2$"),
        nbf.v4.new_code_cell("def compute_cost(X, y, theta):\n    \"\"\"\n    Compute the Mean Squared Error cost.\n    X: Features (including bias column)\n    y: Target values\n    theta: Model parameters\n    \"\"\"\n    m = len(y)\n    predictions = X.dot(theta)\n    error = predictions - y\n    cost = (1/(2*m)) * np.sum(error**2)\n    return cost"),
        nbf.v4.new_markdown_cell("### Gradient Descent Algorithm\n$\\theta_j := \\theta_j - \\alpha \\frac{\partial}{\partial \\theta_j} J(\\theta)$"),
        nbf.v4.new_code_cell("def gradient_descent(X, y, theta, learning_rate, iterations):\n    \"\"\"\n    Perform Gradient Descent to optimize parameters.\n    \"\"\"\n    m = len(y)\n    cost_history = np.zeros(iterations)\n    theta_history = np.zeros((iterations, len(theta)))\n    \n    for i in range(iterations):\n        predictions = X.dot(theta)\n        error = predictions - y\n        \n        # Gradient calculation\n        gradients = (1/m) * X.T.dot(error)\n        \n        # Update parameters\n        theta = theta - learning_rate * gradients\n        \n        theta_history[i,:] = theta.T\n        cost_history[i] = compute_cost(X, y, theta)\n        \n    return theta, cost_history, theta_history"),
        nbf.v4.new_markdown_cell("### Training the Custom Model"),
        nbf.v4.new_code_cell("# Prepare the data: add a bias column (x_0 = 1) to X\nX_b = np.c_[np.ones((100, 1)), X]\n\n# Initialize parameters, learning rate, and iterations\ntheta_initial = np.random.randn(2, 1)  # random initialization\nlearning_rate = 0.1\niterations = 1000\n\n# Run Gradient Descent\ntheta_optimal, cost_history, _ = gradient_descent(X_b, y, theta_initial, learning_rate, iterations)\n\nprint(f\"Optimized Intercept (theta_0): {theta_optimal[0][0]:.4f}\")\nprint(f\"Optimized Slope (theta_1): {theta_optimal[1][0]:.4f}\")\n\n# Visualize Cost History\nplt.figure(figsize=(8, 5))\nplt.plot(range(iterations), cost_history, 'r-')\nplt.xlabel('Iterations')\nplt.ylabel('Cost function J(theta)')\nplt.title('Cost History over Iterations (Gradient Descent)')\nplt.show()")
    ])
    
    with open(NOTEBOOK_NAME, 'w') as f:
        nbf.write(nb, f)
    print("Stage 3 complete.")
    run_git_command(None, "Implement Linear Regression from scratch using Gradient Descent")
    time.sleep(COMMIT_DELAY)

def add_sklearn_implementation():
    with open(NOTEBOOK_NAME, 'r') as f:
        nb = nbf.read(f, as_version=4)
        
    nb['cells'].extend([
        nbf.v4.new_markdown_cell("## 4. Linear Regression using Scikit-Learn\n\nNow we will use the highly optimized `scikit-learn` library to perform the same task and compare the results."),
        nbf.v4.new_code_cell("# Initialize and train the model\nlin_reg = LinearRegression()\nlin_reg.fit(X, y)\n\nprint(f\"Scikit-Learn Intercept: {lin_reg.intercept_[0]:.4f}\")\nprint(f\"Scikit-Learn Slope: {lin_reg.coef_[0][0]:.4f}\")"),
        nbf.v4.new_markdown_cell("### Comparison and Visualization"),
        nbf.v4.new_code_cell("# Generate predictions for plotting the regression line\nX_new = np.array([[0], [2]])\nX_new_b = np.c_[np.ones((2, 1)), X_new]\n\n# Custom model predictions\ny_predict_custom = X_new_b.dot(theta_optimal)\n\n# Scikit-learn predictions\ny_predict_sklearn = lin_reg.predict(X_new)\n\n# Plot both models\nplt.figure(figsize=(10, 6))\nplt.scatter(X, y, color='blue', alpha=0.5, label='Data points')\nplt.plot(X_new, y_predict_custom, 'r-', linewidth=2, label='Custom Gradient Descent')\nplt.plot(X_new, y_predict_sklearn, 'g--', linewidth=2, label='Scikit-Learn')\nplt.xlabel('X')\nplt.ylabel('y')\nplt.title('Comparison of Custom vs Scikit-Learn Linear Regression')\nplt.legend()\nplt.show()"),
        nbf.v4.new_markdown_cell("## Conclusion\n\nBoth implementations yield near-identical results. The intercept is close to 4, and the slope is close to 3, validating that our custom Gradient Descent algorithm works correctly and is equivalent to Scikit-Learn's Ordinary Least Squares approach for this dataset.")
    ])
    
    with open(NOTEBOOK_NAME, 'w') as f:
        nbf.write(nb, f)
    print("Stage 4 complete.")
    run_git_command(None, "Add Scikit-Learn Implementation and Comparison")

if __name__ == "__main__":
    print("Starting Notebook Generation and Commits...")
    create_initial_notebook()
    add_data_generation()
    add_linear_regression_scratch()
    add_sklearn_implementation()
    print("Done!")
