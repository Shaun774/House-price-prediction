# 🏠 House Price Prediction App

A simple web application that utilizes **Multiple Linear Regression** to predict house prices based on physical attributes. This project demonstrates how to integrate a **Scikit-Learn** model into a **Flask** web environment.



---

## 📖 Overview

The application takes two primary inputs to estimate a property's value:
1.  **Square Footage (Area)**: The size of the house in sq. ft.
2.  **Number of Rooms**: The total count of rooms in the house.

The backend uses a trained linear model to process these inputs and return a rounded prediction to the user interface.

---

## 🛠️ Tech Stack

* **Backend:** [Python](https://www.python.org/)
* **Web Framework:** [Flask](https://flask.palletsprojects.com/)
* **Machine Learning:** [Scikit-Learn](https://scikit-learn.org/)
* **Data Manipulation:** [NumPy](https://numpy.org/)

---

## 🧮 How the Model Works

The model is built on the principle of **Multiple Linear Regression**, which maps the relationship between multiple independent variables and one dependent variable.

The prediction logic follows this formula:

$$y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \epsilon$$

Where:
* $y$ = Predicted Price
* $x_1$ = Area
* $x_2$ = Number of Rooms
* $\beta_n$ = Coefficients learned during training

### Training Data
The model is pre-trained on the following sample set:

| Area ($x_1$) | Rooms ($x_2$) | Price ($y$) |
| :--- | :--- | :--- |
| 800 | 1 | 30 |
| 1000 | 2 | 40 |
| 1200 | 2 | 45 |
| 1500 | 2 | 60 |
| 1800 | 3 | 72 |

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed. You will also need to install the following packages:
```bash
pip install flask numpy scikit-learn
