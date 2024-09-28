# Pizza Price Prediction

This project is a Flask-based web application that predicts the price of a pizza based on selected features like quantity, size, name, and ingredients. The model uses **Linear Regression** and **forward feature selection** to provide accurate price estimates.

## Project Overview

The goal of this project is to predict the price of a pizza by identifying key features that influence the cost. Using feature selection techniques, the model selects the most important features: quantity, size, name, and ingredients, and trains a **Linear Regression** model. The final application is deployed using **Flask**, allowing users to interact with the model through a web interface.

## Libraries Used

- **numpy**: For numerical computations.
- **pandas**: For data manipulation and analysis.
- **scikit-learn (sklearn)**: For building the machine learning model (Linear Regression).
- **joblib**: For saving and loading the model efficiently.
- **pickle**: For serializing the trained model.
- **Flask**: For deploying the model via a web application.
- **sqlite3**: For managing and interacting with the SQLite database to store and retrieve pizza data.

## Features

The model predicts pizza prices based on the following selected features:
- **Quantity**: Number of pizzas.
- **Size**: Size of the pizza (small, medium, large, etc.).
- **Name**: Type of pizza (e.g., Margherita, Pepperoni).
- **Ingredients**: Key ingredients of the pizza (cheese, sauce, toppings, etc.).

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/irfanshaikh911/pizza-price-prediction.git
   cd pizza-price-prediction
