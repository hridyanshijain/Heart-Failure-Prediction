# 💓 Heart Failure Risk Prediction Web App

A machine learning-powered web application that predicts the risk of heart failure based on patient medical data. Built with **Logistic Regression** and **Flask**, this app offers a clean, user-friendly interface to assist in early detection of heart disease risk.

## 🧠 Project Objective

To build a web-based tool using **Logistic Regression** that helps healthcare professionals or individuals assess the likelihood of heart failure by inputting relevant medical attributes.

---

## 🚀 Demo

![App Screenshot](./screenshot.png)  
> _Note: Add your own screenshot or link once hosted._

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python     | Core programming language |
| Flask      | Web framework for UI & backend |
| Scikit-learn | Machine Learning (Logistic Regression) |
| Pandas & NumPy | Data manipulation and preprocessing |
| HTML/CSS   | Frontend interface |
| Pickle     | Model serialization |

---

## 📊 Features

- 🧠 Logistic Regression model trained on clinical dataset
- 📦 Predictive analytics for heart failure risk
- 🔍 Input fields for medical attributes:
  - Age
  - Anaemia
  - High Blood Pressure
  - Ejection Fraction
  - Serum Creatinine
  - Serum Sodium
  - Time
  - Diabetes
  - Smoking
  - Sex
- 💻 Simple and intuitive Flask-powered UI
- ⚖️ Uses `StandardScaler` to normalize input data
- 💾 Pickled ML model for deployment

---

## 🧪 Dataset

Dataset used: **[Heart Failure Clinical Records Dataset](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data)**  
- 299 patient records
- 13 clinical features
- Binary classification: `0` (no heart failure), `1` (can be a heart failure)

---

## 📂 Project Structure


