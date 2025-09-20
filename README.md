# 🔌 Four-Port System Modeling with Linear Regression

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2%2B-orange?logo=scikit-learn)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

A machine learning project that demystifies an unknown electronic system by using linear regression to discover its underlying physical law. This project serves as a practical introduction to the core concepts of modeling, analytics, and the machine learning workflow.

---

## 📖 Table of Contents

1.  [Project Overview](#-project-overview)
2.  [The Problem](#-the-problem)
3.  [The Solution](#-the-solution)
4.  [Key Results](#-key-results)
5.  [How to Run](#-how-to-run)
6.  [Dependencies](#-dependencies)
7.  [Types of Analytics](#-types-of-analytics)
8.  [License](#-license)

---

## 🧠 Project Overview

This project is based on a conceptual problem from a machine learning textbook. The goal is to analyze an unknown "black box" four-port electronic system. By applying current (`I`) as input and measuring voltage (`V`) as output, we use **Linear Regression** to learn the system's behavior and reveal its simple, elegant underlying principle: **Ohm's Law**.

---

## ❓ The Problem

We are presented with an unknown system (`H(θ)`):

The internal parameters (`θ`) of the process are hidden. The task is to build a digital model that can describe, diagnose, predict, and prescribe actions for this system.

---

## 🛠️ The Solution

1.  **Data Collection:** Multiple input currents (`I`) were applied, and corresponding output voltages (`V`) were measured.
2.  **Exploratory Data Analysis (EDA):** A scatter plot of `I` vs. `V` revealed a strong, linear relationship.
3.  **Model Selection:** A **Linear Regression** model (without an intercept) was chosen, hypothesizing the relationship `V = k * I`.
4.  **Model Training:** The model was trained on the collected data using `scikit-learn`.
5.  **Evaluation & Insight:** The model's coefficient was extracted, revealing the system's parameter.

---

## 📊 Key Results

The trained model successfully uncovered the physical law governing the system:

### **Model Equation:**
\[ V = 4.96 \cdot I \]

### **Physical Equivalent:**
The unknown system behaves exactly like a **resistor** with a resistance of **~5 Ω**.
This confirms that the process follows **Ohm's Law**: \( V = I \cdot R \).

![Model Fit Visualization](images/model_fit_plot.png) <!-- If you save the plot, add it to an 'images/' folder and use this link -->
*Scatter plot of the collected data (blue) and the predicted linear relationship (red line) from the model.*

---

---

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/fourport-modeling.git
    cd fourport-modeling
    ```

2.  **(Optional) Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
    Navigate to `notebooks/fourport_analysis.ipynb` and run the cells.

---

## 📦 Dependencies

The main Python libraries used in this project are:
*   Python 3.8+
*   [NumPy](https://numpy.org/)
*   [Scikit-Learn](https://scikit-learn.org/stable/)
*   [Matplotlib](https://matplotlib.org/)
*   [Jupyter](https://jupyter.org/)

Install them all using:
```bash
pip install numpy scikit-learn matplotlib jupyter
```
## 📈 Types of Analytics
This model can be used for all four types of data analytics:

📋 **Descriptive:** What happened? "The output was 25V because the input was 5A."

🔍 **Diagnostic:** Why did it happen? "The high output is expected behavior, not a system error."

🔮 **Predictive:** What will happen? "If input reaches 4A, output will be ~20V."

🎯 **Prescriptive:** What should we do? "Keep input current below 4A to ensure output voltage stays under 20V."

## License
This project is for educational purposes, based on concepts from the linked textbook chapter. Feel free to use the code for learning and teaching.

  <div align="center">
Found this project useful? Please consider giving it a ⭐ on GitHub!
</div>
