import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

class SalesDataAnalyzer:

    def __init__(self, file_path=None):
        self.data = None
        self.current_figure = None
        if file_path:
            self.load_data(file_path)

    def __del__(self):
        try:
            plt.close("all")
        except Exception:
            pass

    def load_data(self, file_path):
        try:
            if not os.path.exists(file_path):
                print(f"Error: File '{file_path}' does not exist.")
                return False
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading file: {e}")
            return False

    def explore_data(self, option):
        if self.data is None:
            print("Please load a dataset first.")
            return

        if option == 1:
            print(self.data.head(5))
        elif option == 2:
            print(self.data.tail(5))
        elif option == 3:
            print("Column Names:")
            for col in self.data.columns:
                print(f"- {col}")
        elif option == 4:
            print("Data Types:")
            print(self.data.dtypes)
        elif option == 5:
            print("Basic Information:")
            self.data.info()
        else:
            print("Invalid exploration choice.")

    def clean_data(self, option, val=None):
        if self.data is None:
            print("Please load a dataset first.")
            return

        missing_count = self.data.isnull().sum().sum()

        if option == 1:
            if missing_count == 0:
                print("No missing values found in the dataset!")
            else:
                print("Rows with missing values:")
                print(self.data[self.data.isnull().any(axis=1)])

        elif option == 2:
            if missing_count == 0:
                print("No missing values found in the dataset!")
            else:
                numeric_cols = self.data.select_dtypes(
                    include=[np.number]
                ).columns
                self.data[numeric_cols] = self.data[numeric_cols].fillna(
                    self.data[numeric_cols].mean()
                )
                print("Missing numeric values filled with column mean.")

        elif option == 3:
            if missing_count == 0:
                print("No missing values found in the dataset!")
            else:
                initial_len = len(self.data)
                self.data.dropna(inplace=True)
                print(
                    f"Dropped {initial_len - len(self.data)} rows containing missing values."
                )

        elif option == 4:
            if missing_count == 0:
                print("No missing values found in the dataset!")
            else:
                self.data.fillna(val, inplace=True)
                print(f"Missing values replaced with '{val}'.")

    def mathematical_operations(self):
        if self.data is None:
            print("Please load a dataset first.")
            return

        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            target_col = numeric_cols[0]
            arr = self.data[target_col].to_numpy()
            print(f"\n--- NumPy Array Indexing & Slicing for '{target_col}' ---")
            print(f"NumPy Array: {arr}")
            print(f"First 3 elements (slicing arr[:3]): {arr[:3]}")
            print(f"Element-wise Array Mean: {np.mean(arr):.2f}")
            print(f"Element-wise Standard Deviation: {np.std(arr):.2f}")
        else:
            print("No numeric column available for mathematical operations.")

    def combine_data(self, other_dataframe, method="concat"):
        if self.data is None:
            print("Please load a dataset first.")
            return

        if method == "concat":
            self.data = pd.concat(
                [self.data, other_dataframe], ignore_index=True
            )
            print("DataFrames concatenated successfully.")
        elif method == "merge":
            common = list(
                set(self.data.columns).intersection(set(other_dataframe.columns))
            )
            if common:
                self.data = pd.merge(
                    self.data, other_dataframe, on=common[0], how="inner"
                )
                print(f"DataFrames merged on '{common[0]}'.")
            else:
                print("No common columns found to merge.")

    def split_data(self, split_by_col):
        if self.data is None:
            print("Please load a dataset first.")
            return {}

        if split_by_col in self.data.columns:
            subsets = {
                val: group for val, group in self.data.groupby(split_by_col)
            }
            print(
                f"DataFrame successfully split into {len(subsets)} subsets based on '{split_by_col}'."
            )
            return subsets
        else:
            print(f"Column '{split_by_col}' not found.")
            return {}

    def search_sort_filter(self):
        if self.data is None:
            print("Please load a dataset first.")
            return

        print("\n1. Search for a specific value")
        print("2. Sort by column")
        print("3. Filter by numeric threshold")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            col = input("Enter column name: ").strip()
            val = input("Enter search term: ").strip()
            if col in self.data.columns:
                matches = self.data[
                    self.data[col].astype(str).str.contains(val, case=False, na=False)
                ]
                print(f"Found {len(matches)} matching record(s):")
                print(matches)
            else:
                print("Column not found.")

        elif choice == "2":
            col = input("Enter column to sort by: ").strip()
            order = input("Ascending? (y/n): ").strip().lower() == "y"
            if col in self.data.columns:
                print(self.data.sort_values(by=col, ascending=order).head(10))
            else:
                print("Column not found.")

        elif choice == "3":
            col = input("Enter numeric column: ").strip()
            val = float(input("Enter minimum threshold value: ").strip())
            if col in self.data.columns:
                print(self.data[self.data[col] >= val])
            else:
                print("Column not found.")

    def statistical_analysis(self):
        if self.data is None:
            print("Please load a dataset first.")
            return

        print("\n== Descriptive Statistics ==")
        print(self.data.describe())

        numeric_df = self.data.select_dtypes(include=[np.number])
        if not numeric_df.empty:
            print("\nVariance:")
            print(numeric_df.var())
            print("\nStandard Deviation:")
            print(numeric_df.std())
            print("\nPercentiles (25%, 50%, 75%):")
            print(numeric_df.quantile([0.25, 0.50, 0.75]))

    def create_pivot_table(self):
        if self.data is None:
            print("Please load a dataset first.")
            return

        print(f"Columns: {list(self.data.columns)}")
        index_col = input("Enter row index column (e.g., Region): ").strip()
        val_col = input("Enter values column (e.g., Sales): ").strip()

        if index_col in self.data.columns and val_col in self.data.columns:
            pivot = pd.pivot_table(
                self.data, index=index_col, values=val_col, aggfunc=["mean", "sum"]
            )
            print("\nGenerated Pivot Table:")
            print(pivot)
        else:
            print("Invalid column names.")

    def visualize_data(self, plot_type):
        if self.data is None:
            print("Please load a dataset first.")
            return

        sns.set_theme(style="whitegrid")
        fig, ax = plt.subplots(figsize=(8, 5))

        if plot_type == 1:
            x = input("Enter x-axis column name: ").strip()
            y = input("Enter y-axis column name: ").strip()
            if x in self.data.columns and y in self.data.columns:
                sns.barplot(data=self.data, x=x, y=y, ax=ax, estimator=np.sum, errorbar=None)
                ax.set_title(f"Bar Plot: {y} by {x}")
                ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
            else:
                print("Specified columns not found.")
                return

        elif plot_type == 2:
            x = input("Enter x-axis column name: ").strip()
            y = input("Enter y-axis column name: ").strip()
            if x in self.data.columns and y in self.data.columns:
                sns.lineplot(data=self.data, x=x, y=y, marker="o", ax=ax)
                ax.set_title(f"Line Plot: {y} vs {x}")
            else:
                print("Specified columns not found.")
                return

        elif plot_type == 3:
            x = input("Enter x-axis column name: ").strip()
            y = input("Enter y-axis column name: ").strip()
            if x in self.data.columns and y in self.data.columns:
                print("Generating scatter plot...")
                sns.scatterplot(data=self.data, x=x, y=y, s=80, ax=ax)
                ax.set_title(f"Scatter Plot: {y} vs {x}")
                print("Scatter plot displayed successfully!")
            else:
                print("Specified columns not found.")
                return

        elif plot_type == 4:  
            col = input("Enter category column for Pie Chart: ").strip()
            if col in self.data.columns:
                counts = self.data[col].value_counts()
                ax.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=140)
                ax.set_title(f"Distribution of {col}")
            else:
                print("Specified column not found.")
                return

        elif plot_type == 5:  
            col = input("Enter numeric column name for Histogram: ").strip()
            if col in self.data.columns:
                sns.histplot(self.data[col], kde=True, ax=ax)
                ax.set_title(f"Histogram: {col}")
            else:
                print("Specified column not found.")
                return

        elif plot_type == 6: 
            x_col = input("Enter sequence/x column (e.g., Year): ").strip()
            num_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
            if x_col in num_cols:
                num_cols.remove(x_col)
            if x_col in self.data.columns and len(num_cols) >= 2:
                pivot_stack = self.data.groupby(x_col)[num_cols[:3]].sum()
                ax.stackplot(
                    pivot_stack.index.astype(str),
                    [pivot_stack[c] for c in pivot_stack.columns],
                    labels=pivot_stack.columns,
                )
                ax.legend(loc="upper left")
                ax.set_title("Stack Plot")
            else:
                print("Not enough numeric dimensions for stack plot.")
                return

        self.current_figure = fig
        plt.tight_layout()
        plt.show()

    def save_visualization(self, filename):

        if self.current_figure is None:
            print("No active visualization found to save. Generate a plot first.")
            return

        try:
            self.current_figure.savefig(filename, dpi=300)
            print(f"Visualization saved as {filename} successfully!")
        except Exception as e:
            print(f"Failed to save visualization: {e}")


class AdvancedSalesAnalyzer(SalesDataAnalyzer):

    def __init__(self, file_path=None):
        super().__init__(file_path)

    def __add__(self, other):
        if isinstance(other, SalesDataAnalyzer) and other.data is not None:
            new_analyzer = AdvancedSalesAnalyzer()
            new_analyzer.data = pd.concat([self.data, other.data], ignore_index=True)
            return new_analyzer
        return self
def create_default_data_file():
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", "sales_data.csv")
    if not os.path.exists(file_path):
        sample_df = pd.DataFrame(
            {
                "SalesID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
                "Product": [
                    "Product A",
                    "Product B",
                    "Product C",
                    "Product D",
                    "Product E",
                    "Product A",
                    "Product B",
                    "Product C",
                    "Product D",
                    "Product E",
                ],
                "Region": [
                    "North",
                    "East",
                    "West Coast",
                    "South",
                    "Central",
                    "East",
                    "North",
                    "South",
                    "West Coast",
                    "Central",
                ],
                "Sales": [500, 600, 700, 800, 550, 620, 710, 850, 900, 600],
                "Profit": [120, 150, 210, 240, 110, 130, 190, 260, 310, 140],
                "Year": [2022, 2022, 2022, 2022, 2022, 2023, 2023, 2023, 2023, 2023],
            }
        )
        sample_df.to_csv(file_path, index=False)


# =======================================================
# 4. Interactive Console User Interface (Menu Loop)
# =======================================================
def display_main_menu():
    print("========== Data Analysis & Visualization Program ==========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("============================================================")


def main():
    create_default_data_file()
    analyzer = AdvancedSalesAnalyzer()

    while True:
        display_main_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("\n== Load Dataset ==")
            path = input("Enter the path of the dataset (CSV file): ").strip()
            analyzer.load_data(path)
            print()

        elif choice == "2":
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            sub_choice = input("Enter your choice: ").strip()
            if sub_choice.isdigit():
                analyzer.explore_data(int(sub_choice))
            print()

        elif choice == "3":
            print("\n== DataFrame Operations ==")
            print("1. Search, Sort, or Filter Data")
            print("2. NumPy Array Operations & Slicing")
            print("3. Create Pivot Table")
            print("4. Split Data by Category")
            sub_choice = input("Enter your choice: ").strip()
            if sub_choice == "1":
                analyzer.search_sort_filter()
            elif sub_choice == "2":
                analyzer.mathematical_operations()
            elif sub_choice == "3":
                analyzer.create_pivot_table()
            elif sub_choice == "4":
                col = input("Enter column name to split by: ").strip()
                analyzer.split_data(col)
            print()

        elif choice == "4":
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            sub_choice = input("Enter your choice: ").strip()
            if sub_choice in ["1", "2", "3"]:
                analyzer.clean_data(int(sub_choice))
            elif sub_choice == "4":
                val = input("Enter replacement value: ").strip()
                analyzer.clean_data(4, val)
            print()

        elif choice == "5":
            analyzer.statistical_analysis()
            print()

        elif choice == "6":
            print("\n== Data Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            sub_choice = input("Enter your choice: ").strip()
            if sub_choice.isdigit():
                analyzer.visualize_data(int(sub_choice))
            print()

        elif choice == "7":
            print("\n== Save Visualization ==")
            filename = input(
                "Enter file name to save the plot (e.g., scatter_plot.png): "
            ).strip()
            analyzer.save_visualization(filename)
            print()

        elif choice == "8":
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose a valid option (1-8).\n")


if __name__ == "__main__":
    main()