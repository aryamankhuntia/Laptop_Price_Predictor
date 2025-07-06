# 💻 Laptop Price Prediction Model

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Framework](https://img.shields.io/badge/Framework-Flask-red)](https://flask.palletsprojects.com/)
[![Deployment](https://img.shields.io/badge/Deployment-AWS-purple)](https://aws.amazon.com/)

A machine learning model that predicts laptop prices based on specifications, with a web interface for real-time predictions.

👉 **Live Demo:** [http://ec2-3-93-145-120.compute-1.amazonaws.com/](http://ec2-3-93-145-120.compute-1.amazonaws.com/)

![App Screenshot](/screenshots/interface.jpg) 

## Problem Statement
Most tech companies face a plethora of decisions to be made to optimize their products and keep their brands relevent in the evergrowing and competitive market for tech. New-age laptops are one such important decision, wherein companies are unable to predict what specifications are profitable to beat out competition, which means finding the fine line between investment into more optimized specifications and fulfilling consumer buy-in. This app helps make these decisions by tracking projected market starter prices to predict what products are required by the company to invest in.

## ✨ Features
- Predicts starter prices of new laptop models based on hand-engineered specifications
- Intuitive web interface 
- Starter prices given a higher average value to handle market retention goals

## 🛠️ Installation
To run locally:
```bash
# Clone repository
git clone https://github.com/your-username/laptop-price-predictor.git

# Install dependencies
pip install -r requirements.txt

# Start Flask server
python app.py
