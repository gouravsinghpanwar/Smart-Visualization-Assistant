import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Create main window
root = tk.Tk()
root.title("Basic Visualization Assistant")
root.geometry("750x520")

df = None


# ---------------- FILE UPLOAD ----------------
def upload_file():
    global df

    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
    )

    if not file_path:
        return

    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)

        messagebox.showinfo("Success", "File loaded successfully!")
        show_basic_info()

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- DATASET INFO ----------------
def show_basic_info():
    global df

    if df is None:
        return

    info_text.delete("1.0", tk.END)

    info_text.insert(tk.END, f"Dataset Shape: {df.shape}\n\n")

    info_text.insert(tk.END, "Columns:\n")
    for col in df.columns:
        info_text.insert(tk.END, f"- {col}\n")

    info_text.insert(tk.END, "\nData Types:\n")
    info_text.insert(tk.END, f"{df.dtypes}\n")

    info_text.insert(tk.END, "\nMissing Values:\n")
    info_text.insert(tk.END, f"{df.isnull().sum()}\n")


# ---------------- MAIN LOGIC ----------------
def analyze_and_visualize():
    global df

    if df is None:
        messagebox.showwarning("Warning", "Upload a file first!")
        return

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    plt.figure()

    # -------- Case 1: Only ONE numeric column --------
    if len(numeric_cols) == 1 and len(categorical_cols) == 0:
        col = numeric_cols[0]

        plt.hist(df[col], bins=20)
        plt.title(f"{col} Distribution")
        plt.xlabel(col)
        plt.ylabel("Frequency")

        messagebox.showinfo("Insight",
            f"Histogram used because dataset has one numeric variable ({col}).")

    # -------- Case 2: Only ONE categorical column --------
    elif len(categorical_cols) == 1 and len(numeric_cols) == 0:
        col = categorical_cols[0]

        df[col].value_counts().plot(kind='bar')
        plt.title(f"{col} Count")

        messagebox.showinfo("Insight",
            f"Bar chart used because dataset has one categorical variable ({col}).")

    # -------- Case 3: Multiple numeric columns --------
    elif len(numeric_cols) >= 2:
        # Select top 2 columns with highest variance
        variances = df[numeric_cols].var().sort_values(ascending=False)
        col1 = variances.index[0]
        col2 = variances.index[1]

        plt.scatter(df[col1], df[col2])
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.title(f"{col1} vs {col2}")

        messagebox.showinfo("Insight",
            f"Scatter plot used for relationship between '{col1}' and '{col2}' (highest variance).")

    # -------- Case 4: Mixed (numeric + categorical) --------
    elif len(numeric_cols) >= 1 and len(categorical_cols) >= 1:
        # Select numeric with highest variance
        num_var = df[numeric_cols].var().sort_values(ascending=False).index[0]

        # Select categorical with limited categories (avoid clutter)
        cat_var = None
        for col in categorical_cols:
            if df[col].nunique() <= 10:
                cat_var = col
                break

        if cat_var:
            grouped = df.groupby(cat_var)[num_var].mean()

            grouped.plot(kind='bar')
            plt.title(f"{num_var} by {cat_var}")
            plt.ylabel("Average Value")

            messagebox.showinfo("Insight",
                f"Bar chart shows average '{num_var}' across categories of '{cat_var}'.")
        else:
            messagebox.showinfo("Info", "Categorical data has too many unique values.")

    else:
        messagebox.showinfo("Info", "No suitable visualization found.")

    plt.tight_layout()
    plt.show()


# ---------------- UI ----------------
title = tk.Label(root, text="Basic Visualization Assistant", font=("Arial", 16))
title.pack(pady=10)

upload_btn = tk.Button(root, text="Upload CSV / Excel File", command=upload_file)
upload_btn.pack(pady=8)

info_text = tk.Text(root, height=16, width=85)
info_text.pack(padx=10, pady=10)

analyze_btn = tk.Button(root, text="Analyze & Visualize", command=analyze_and_visualize)
analyze_btn.pack(pady=10)

root.mainloop()