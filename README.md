# 🎨 Smart Visualization Assistant
### Data Science Foundation — Course Project
**Submitted by:** Gourav Singh Panwar (AU23B1009)
**Submitted to:** Prof. Deepak Yadav Sir

---

## 📌 What is this project?

A rule-based desktop application that **automatically analyzes any CSV/Excel dataset** and generates the most suitable visualization — without the user needing to manually select a chart type. It also explains *why* that chart was chosen, making it perfect for data science beginners.

---

## ⚙️ How It Works — Decision Engine

The system applies 4 smart rules based on dataset structure:

| Case | Condition | Chart Selected | Reason |
|---|---|---|---|
| 1 | Only 1 numeric column | Histogram | Shows distribution |
| 2 | Only 1 categorical column | Bar Chart | Shows frequency |
| 3 | 2+ numeric columns | Scatter Plot | Uses top 2 highest-variance columns |
| 4 | Numeric + Categorical | Grouped Bar Chart | Average numeric value per category |

---

## 🚀 How to Run

### Step 1 — Clone the repository
```bash
git clone https://github.com/YourUsername/Smart-Visualization-Assistant.git
cd Smart-Visualization-Assistant
```

### Step 2 — Install required libraries
```bash
pip install pandas matplotlib openpyxl
```
> Note: `tkinter` comes built-in with Python. No separate install needed.

### Step 3 — Run the app
```bash
python data_analyzer.py
```

---

## 📋 Requirements

| Library | Purpose |
|---|---|
| `tkinter` | GUI (built-in with Python) |
| `pandas` | Data loading and processing |
| `matplotlib` | Chart generation |
| `openpyxl` | Reading Excel files |

**Python version:** 3.7+

---

## 🗂️ Project Structure

```
📦 Smart-Visualization-Assistant
 ┣ 📄 data_analyzer.py       ← Main application file
 ┣ 📄 Report.pdf             ← Full project report
 ┣ 📂 screenshots/           ← App and output screenshots
 ┗ 📄 README.md
```

---

## 🧠 Key Concepts Used

- **Variance-based column selection** — picks the most informative numeric columns for scatter plots
- **Unique value count** — avoids cluttered charts by limiting categorical columns to ≤10 unique values
- **Rule-based decision logic** — transparent, explainable, no ML required
- **Tkinter GUI** — fully interactive desktop interface

---

## ✅ Features

- Upload CSV or Excel datasets with one click
- Auto-detects column data types (numeric vs categorical)
- Displays dataset shape, columns, data types, and missing values
- Generates appropriate chart automatically
- Shows an insight message explaining the chart choice
- No coding knowledge required to use

---

## ⚠️ Limitations

- Supports basic chart types only (histogram, bar, scatter)
- No time-series or date detection
- No domain-specific reasoning
- Works best on small to medium datasets

---

## 🔮 Future Enhancements

- Add line charts for time-series data
- Add box plots and heatmaps
- Improve chart selection using ML
- Build a web-based version using Streamlit

---

## 🛠️ Tech Stack

`Python` `Tkinter` `Pandas` `Matplotlib`

---
