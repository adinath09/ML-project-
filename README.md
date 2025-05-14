## End to End to Machine Learning project 


# 🧠 Student Performance Indicator 

This project predicts a student’s math score based on various attributes such as gender, parental education level, lunch type, test preparation course, reading score, and writing score. The model is deployed using **AWS Elastic Beanstalk** for production.

---

## 🚀 Features

- **Data Preprocessing:** Uses pipelines (e.g., `Pipeline`, `ColumnTransformer`) for numerical and categorical features.
- **Model Training:** Implements machine learning model training and evaluation.
- **REST API:** A Flask API serves predictions.
- **Deployment Ready:** Deployed on AWS Elastic Beanstalk.
- **Logging & Exception Handling:** Custom logging and exception mechanisms.

---

## 📂 Project Structure

```

├── .elasticbeanstalk/         # Elastic Beanstalk configuration files
├── artifacts/                 # Directory for storing serialized model/pipeline objects
├── src/                       # Source code package
│   ├── components/            # Data transformation, model training components
│   ├── pipelines/             # Training and prediction pipelines
│   ├── exception.py           # Custom exception classes
│   ├── logger.py              # Logging configuration and setup
│   └── utils.py               # Utility functions (e.g., save\_object)
├── app.py                     # Flask app entry point for local development
├── application.py             # WSGI entry point for Elastic Beanstalk deployment
├── requirements.txt           # Python dependencies
├── setup.py                   # Setup configuration for packaging
└── README.md                  # This file

````


## 🧪 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-performance-indicator.git
cd student-performance-indicator
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

Run the training pipeline to preprocess the data and train the model:

```bash
python src/pipelines/train_pipeline.py
```

### 5. Run the App Locally

Start the Flask application:

```bash
python app.py
```

Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## ☁️ Deployment: AWS Elastic Beanstalk

### Prerequisites

* [AWS Elastic Beanstalk CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html) installed
* AWS credentials configured

### Deployment Steps

1. **Initialize Elastic Beanstalk**

   ```bash
   eb init -p python-3.8 student-performance-eb --region <your-region>
   ```

2. **Create an Environment**

   ```bash
   eb create student-performance-env
   ```

3. **Deploy the Application**

   ```bash
   eb deploy
   ```

4. **Open the Deployed App**

   ```bash
   eb open
   ```

---

## 📦 Requirements

* Python 3.8+
* scikit-learn
* pandas
* numpy
* Flask
* gunicorn (for production deployment)

All dependencies are listed in the `requirements.txt` file.

---

## 🧠 Model Information

* **Input Features:** Gender, Race/Ethnicity, Parental Level of Education, Lunch, Test Preparation Course, Reading Score, Writing Score
* **Target:** Math Score
* **Model:** Regression model (e.g., LinearRegression, RandomForestRegressor) with evaluation metrics such as RMSE, MAE, and R².


## 🙋‍♂️ Author

* [Adinath Nage](https://github.com/adinath09)
* Email: adinathnage939@gmail.com

---

## 🔗 Demo
![jj](https://github.com/user-attachments/assets/ce08a8d8-3ba3-4e56-9e8a-e881d99dc4df)



