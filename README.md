# 📊 Study Grade Predictor

This is a beginner-friendly Python project where I tried to understand how machine learning works by building a simple grade predictor from scratch. It uses study hours to predict student marks using basic linear regression, without using any external libraries. The goal of this project is to learn the core idea behind predicti

---

## 🚀 Features

* 📈 Linear Regression (implemented manually, no libraries)
* 🧠 Predict grades based on study hours
* 📉 Error calculation using **MAE (Mean Absolute Error)**
* 🎯 Accuracy measurement using **R² Score**
* 📊 Terminal-based bar chart visualization
* 💻 User input for personalized prediction

---

## 🛠️ Technologies Used

* Python (No external libraries)

---

## 📂 Project Structure

```
study-grade-predictor/
│
├── main.py        # Main program file
└── README.md      # Project documentation
```

---

## ⚙️ How It Works

1. Takes sample data:

   * Study hours
   * Grades

2. Calculates:

   * Average values
   * Slope and intercept of regression line

3. Builds equation:

```
grade = slope × study_hours + intercept
```

4. Predicts grades and evaluates performance using:

   * MAE (error)
   * R² (accuracy)

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/study-grade-predictor.git
```

2. Navigate to the folder:

```
cd study-grade-predictor
```

3. Run the program:

```
python main.py
```

---

## 🧪 Example Output

```
Slope     : 5.60
Intercept : 32.10

Study: 5hrs | Actual: 63 | Predicted: 60.2

Average Error (MAE) : 3.50 marks
Accuracy (R²)       : 0.95


## 🎯 Future Improvements

* Add multiple variables (sleep, attendance)
* Build a GUI (Tkinter / Web App)
* Use real datasets
* Compare with sklearn implementation

## 📌 Author

Made by **Chaitanya Babuta**

## ⭐ Contribute

Feel free to fork this repo and improve it!
