# Healthcare Cost Prediction Model

## Overview

In this project, we predict healthcare costs using a regression algorithm. The dataset contains information about individuals, including their healthcare costs, and the goal is to build a model that can accurately predict healthcare expenses based on the given features.

### Objective
The task is to create a model that predicts healthcare costs using the `train_dataset`. The model is evaluated on an unseen `test_dataset` to determine how well it generalizes. The goal is for the model to achieve a **Mean Absolute Error (MAE)** of under **$3500**, meaning it predicts healthcare costs within $3500 of the actual values.

## Dataset
The dataset contains various features about individuals, such as:
- **Age**
- **Gender**
- **BMI (Body Mass Index)**
- **Children**
- **Smoker status**
- **Region**
- **Healthcare costs** (target variable)

You can download the dataset from [this link](https://cdn.freecodecamp.org/project-data/health-costs/insurance.csv), or use the following command to download directly:
```bash
!wget https://cdn.freecodecamp.org/project-data/health-costs/insurance.csv
```

## Model & Approach

- **Data Preprocessing**: Clean and preprocess the dataset, handling missing values, encoding categorical variables, and scaling the data as needed.
- **Model Building**: Train a regression model using the train_dataset.
- **Evaluation**: Use **Mean Absolute Error (MAE)** to evaluate the model's performance. The model should achieve an MAE under **3500** to pass the challenge.
- **Testing**: The final cell in the notebook uses the `test_dataset` to check the model's performance on unseen data and graph the predicted vs. actual healthcare costs.


## Project Files

- `predict_health_costs_with_regression.ipynb`: The Jupyter notebook containing the full implementation of data preprocessing, model training, evaluation, and testing.
- `insurance.csv`: The dataset used to train and test the model (downloadable via the provided link or wget command).
- `Healthcare_cost_regressor.pkl`: The trained model saved as a pickle file for reuse.

## Getting Started

1. **Clone the Repository**:
```bash
   git clone https://github.com/tadiwosgetachew/machine_learning_projects/healthcare-cost-calculator.git
```
2. **Requirements**:
```bash
   pip install -r requirements.txt
```
3. **Run the Jupyter Notebook**: Open `predict_health_costs_with_regression.ipynb` and run each cell to preprocess the data, train the model, and evaluate its performance.
   
## Acknowledgments

- scikit-learn for providing the tools for building the regression model.
- TensorFlow/Keras for deep learning capabilities.
- The dataset from freeCodeCamp for providing valuable real-world data.

## Contributions

Contributions are welcome! Feel free to fork the repository, make improvements, or open an issue to suggest changes or report bugs.

## Conclusion

This project demonstrates how machine learning can be used to predict healthcare costs based on various individual features. The goal is to build a model that can generalize well to new, unseen data, providing accurate predictions within a specified range.




