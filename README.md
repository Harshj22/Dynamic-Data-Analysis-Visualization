# Dynamic Data Analysis & Visualization System 📊

## 🔍 Project Overview
This project is a fully **dynamic, user-driven data analysis and visualization system** built using Python.
Unlike static projects that work on a fixed dataset, this system allows users to load **any CSV dataset**,
explore its structure, handle missing values using multiple strategies, and generate a wide range of
visualizations based on user-selected parameters.

The project simulates a real-world **Exploratory Data Analysis (EDA) workflow** and is designed to be
reusable, interactive, and scalable.

---

## 🎯 Project Objectives
- To build a dynamic system that works with **any CSV dataset**
- To allow users to **explore datasets interactively**
- To provide multiple **missing value handling techniques**
- To generate **custom visualizations** based on user input
- To demonstrate practical application of data analysis concepts using Python

---

## ⚙️ Key Features

### 📁 Dynamic Dataset Loading
- User can load any CSV file by providing the file path
- Incorrect file paths are handled gracefully with retry options
- Program does not terminate on input errors

---

### 📊 Dataset Exploration Module
Users can dynamically view:
- First 5 rows (head)
- Last 5 rows (tail)
- Dataset structure and data types (`info`)
- Column names
- Statistical summary (`describe`)
- Missing values count (`isnull().sum()`)

---

### 🧹 Missing Value Handling (User-Controlled)
The system provides multiple strategies to handle missing values:
- Drop rows containing missing values
- Fill numerical columns using:
  - Mean
  - Median
- Fill categorical columns using:
  - Mode
- Combined strategy (numerical = median, categorical = mode)
- Drop entire columns dynamically

This ensures flexibility for different datasets and real-world scenarios.

---

### 📈 Dynamic Visualization Engine
Users can choose:
- Visualization type **before** selecting columns
- X-axis, Y-axis, and optional Hue column dynamically

Supported charts:
- Line Plot
- Bar Plot
- Scatter Plot
- Box Plot
- Violin Plot
- Histogram
- Pie Chart

Visualization parameters such as color palettes and figure size are pre-configured for professional output.

---

## 🧠 Why This Project Is Different
- ❌ Not limited to a single dataset (e.g., Titanic)
- ❌ No hard-coded column names
- ✅ Fully dynamic and reusable
- ✅ Menu-driven and interactive
- ✅ Real-world data analysis workflow
- ✅ User makes all analytical decisions

This makes the project closer to a **data analysis tool** rather than a simple assignment.

---

## 🛠️ Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn

---

## ▶️ How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/dynamic-data-analysis-visualization.git
