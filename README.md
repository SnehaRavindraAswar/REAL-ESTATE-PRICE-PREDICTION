# REAL-ESTATE-PRICE-PREDICTION

![image alt](https://github.com/SnehaRavindraAswar/REAL-ESTATE-PRICE-PREDICTION/blob/main/REPP_website.png?raw=true)


This project is part of a data science series that walks through a step-by-step process of building a real estate price prediction website. The project consists of three major components:

1. **Model Building**: We create a machine learning model using Scikit-learn and Linear Regression with a dataset of Bangalore home prices from Kaggle.
2. **Backend (Python Flask)**: A Python Flask server is built to serve the saved model and handle HTTP requests.
3. **Frontend (HTML/CSS/JavaScript)**: A simple web interface that allows users to input property details such as square footage and the number of bedrooms, which then calls the Flask server to return the predicted price.

## **Features**

- **Data Science Concepts**:
    - Data loading and cleaning
    - Outlier detection and removal
    - Feature engineering
    - Dimensionality reduction
    - Hyperparameter tuning using `GridSearchCV`
    - Model validation using k-fold cross-validation

- **Technologies & Tools**:
    - **Python**: Primary language for model building and backend
    - **Numpy and Pandas**: For data manipulation and cleaning
    - **Matplotlib**: For data visualization
    - **Scikit-learn (Sklearn)**: For model building and evaluation
    - **Flask**: To create the HTTP server for serving the model
    - **HTML/CSS/JavaScript**: For creating the user interface

## **Project Structure**

- `data/`: Contains the dataset (Bangalore home prices)
- `model/`: Code for training and saving the machine learning model
- `server.py`: Python Flask server to handle API requests and serve the model
- `templates/`: HTML, CSS, and JavaScript files for the frontend
