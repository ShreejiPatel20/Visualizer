# Pandas Analyzer & Data Visualization

A comprehensive Sales Data Analysis and Visualization tool developed in Python. This project utilizes **Pandas** for structured data manipulation, **NumPy** for array-level computations and slicing, and **Matplotlib** / **Seaborn** for exploratory visual analytics. The entire system is built around Object-Oriented Programming (OOP) principles and offers an interactive console-driven interface.

---

## 📌 Project Overview & Objectives

- **Data Exploration & Preprocessing**: Systematic handling of real-world sales records, inspection of schema details, missing value imputation, and type conversions.
- **Mathematical & Array Operations**: Conversion of DataFrame subsets into NumPy arrays to leverage vectorization, element-wise statistics, and multi-axis slicing.
- **Advanced Data Aggregation**: Multi-dimensional pivot table creation, grouped data transformation, and conditional subset splitting.
- **Data Visualization**: Rich visual reporting using Matplotlib and Seaborn (Bar, Line, Scatter, Pie, Histogram, Stack Plots) with export capabilities.
- **Object-Oriented Design**: Clean encapsulation inside the `SalesDataAnalyzer` base class and `AdvancedSalesAnalyzer` subclass featuring operator overloading and inheritance.

---

## 🏗️ Architecture & OOP Design

The core logic is structured within modular classes:

- **`SalesDataAnalyzer`**:
  - `__init__(file_path)`: Initializes dataset attributes and loads initial CSV data.
  - `__del__()`: Cleans up active plot instances and figures on teardown.
  - `load_data(file_path)`: Robust CSV ingestion with exception handling.
  - `explore_data(option)`: Inspects head/tail slices, schema info, and data types.
  - `clean_data(option, val)`: Detects null fields, applies mean imputation, or removes bad records.
  - `mathematical_operations()`: Demonstrates NumPy conversions, array slicing, and element-wise computations.
  - `combine_data(other_dataframe, method)`: Joins or concatenates datasets dynamically.
  - `split_data(split_by_col)`: Segregates records into localized categorical DataFrames.
  - `search_sort_filter()`: Implements regex matching, multi-column sorting, and threshold filtering.
  - `statistical_analysis()`: Computes variance, standard deviations, and quartile distributions.
  - `create_pivot_table()`: Summarizes sales metrics across categories and time frames.
  - `visualize_data(plot_type)`: Generates customizable Seaborn/Matplotlib figures.
  - `save_visualization(filename)`: Persists active plots as high-resolution images (`.png`, `.jpg`).
- **`AdvancedSalesAnalyzer(SalesDataAnalyzer)`**:
  - Demonstrates inheritance, using `super()` to initialize base configurations.
  - Implements **Operator Overloading** (`__add__`) to allow natural combination of two analyzer objects: `combined_analyzer = analyzer1 + analyzer2`.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed along with the required scientific libraries:

```bash
pip install pandas matplotlib seaborn numpy
```

### Repository Structure

```text
├── data/
│   └── sales_data.csv        # Default or synthetic sales dataset
├── main.py                   # Complete application script
├── README.md                 # Project documentation
└── output_plots/             # Directory for exported charts (optional)
```

### Running the Application

Execute the application from your terminal or Jupyter environment:

```bash
python main.py
```

---

## 💻 Console Interaction Workflow

The application runs a menu-driven CLI interface matching standard workflow requirements:

```text
========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
============================================================
```

1. **Load Dataset**: Provide the path to your CSV file (e.g., `data/sales_data.csv`).
2. **Explore Data**: Check the first/last rows, column types, or summary layout.
3. **Perform DataFrame Operations**: Run NumPy slicing, query filters, category splits, or pivot summaries.
4. **Handle Missing Data**: Identify null entries and replace them with mean values or custom markers.
5. **Generate Descriptive Statistics**: View 5-number summaries, standard deviation, and variance.
6. **Data Visualization**: Generate your plot of choice (Scatter, Bar, Line, Pie, Histogram, Stack Plot).
7. **Save Visualization**: Enter an export target (e.g., `scatter_plot.png`) to save the plot.

---

## ⚙️ Assumptions & Design Notes

1. **Dataset Schema**: The default synthetic generator creates fields for `SalesID`, `Product`, `Region`, `Sales`, `Profit`, and `Year`. When using custom datasets, ensure columns are referenced appropriately during interactive prompts.
2. **Missing Values**: Imputation with column means is restricted to numeric columns (`select_dtypes(include=[np.number])`) to maintain data integrity.
3. **Plot Caching**: The most recently created figure is retained in memory under `self.current_figure` so that option `7. Save Visualization` can capture it without regenerating calculations.
4. **Plot Cleanup**: `__del__` invokes `plt.close('all')` to prevent memory leaks during long-running sessions or automated testing.

---

## 📄 License & Attribution

This project is created for academic and educational evaluation. All code is original and adheres strictly to course submission standards.