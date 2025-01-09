# 💵 Salary Prediction System

This project is a **Salary Prediction System** that uses a Machine Learning model to predict salaries based on input features. The project is structured into backend, frontend, and machine learning components, with a virtual environment for managing dependencies.

**Move to master branch for files**

## 📂 Project Structure

```
Salary_Prediction
├── backend
│   ├── prediction
│   └── salary_prediction
│       ├── db.sqlite3
│       └── manage.py
├── frontend
│   └── app.py
├── ml_model
│   ├── label_encoder.pkl
│   ├── salary_model.pkl
│   └── train_model.py
├── venv
│   ├── Lib
│   ├── Scripts
│   └── pyvenv.cfg
```

### 🔑 Key Directories and Files

- **backend**: Contains backend code for handling API requests and interactions with the database.
  - 📄 `db.sqlite3`: SQLite database file for storing application data.
  - ⚙️ `manage.py`: Django management script.

- **frontend**: Contains the frontend application code.
  - 💻 `app.py`: Main entry point for the frontend application.

- **ml_model**: Contains machine learning components.
  - 🛠️ `train_model.py`: Script for training the salary prediction model.
  - 📦 `salary_model.pkl`: Serialized machine learning model.
  - 🔧 `label_encoder.pkl`: Serialized label encoder for preprocessing categorical features.

- **venv**: Python virtual environment for managing project dependencies.

## 🚀 Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd Salary_Prediction
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   Navigate to the `backend` directory and run:
   ```bash
   python manage.py migrate
   ```

5. **Run Backend Server**:
   ```bash
   python manage.py runserver
   ```

6. **Run Frontend Application**:
   Navigate to the `frontend` directory and run:
   ```bash
   python app.py
   ```

7. **Train the Model (Optional)**:
   If you want to retrain the model, navigate to the `ml_model` directory and run:
   ```bash
   python train_model.py
   ```

## ✨ Features

- 🛠️ **Backend**: Django-based backend to handle API requests and database management.
- 💻 **Frontend**: Python-based frontend interface.
- 🤖 **Machine Learning**: Pretrained model for salary prediction using pickle for serialization.
- 🗄️ **Database**: SQLite database for managing persistent data.

## 🛠️ Technologies Used

- **Backend**: Django, SQLite
- **Frontend**: HTML/CSS (assumed based on `app.py`)
- **Machine Learning**: scikit-learn, pickle
- **Environment Management**: Python `venv`

## 🌱 Future Enhancements

- ✅ Add more robust data validation and preprocessing.
- 📊 Integrate advanced visualization tools for displaying predictions.
- ☁️ Deploy the project using a cloud platform like AWS or Heroku.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🙏 Acknowledgments

- 🌟 Inspired by real-world salary prediction use cases.
- 💖 Special thanks to contributors and open-source libraries used in this project.
