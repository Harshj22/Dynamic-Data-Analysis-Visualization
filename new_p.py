import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
print("\n===== Dynamic Data Analysis & Visualization System =====\n")

def load_dataset():
    while True:
        path = input("\nEnter any CSV file path: ")

        try:
            df = pd.read_csv(path)
            print("\nDataset loaded successfully!")
            return df
        except Exception as e:
            print("\nError loading dataset.")
            print("Reason:", e)
            print("Please try again.")


def dataset_info_menu(df):
    while True:
        print("\n--- DATASET INFORMATION MENU ---\n")
        print("1. Show first 5 rows (Head)")
        print("2. Show last 5 rows (Tail)")
        print("3. Show Dataset Info")
        print("4. Show Column Names")
        print("5. Show statistical Describe")
        print("6. Show Missing values count")
        print("0. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            print(df.head())
        elif ch == "2":
            print(df.tail())
        elif ch == "3":
            print(df.info())
        elif ch == "4":
            print(list(df.columns))
        elif ch == "5":
            print(df.describe())
        elif ch == "6":
            print(df.isnull().sum())
        elif ch == "0":
            break
        else:
            print("Invalid choice!")


def handle_missing_values(df):
    print("\nCurrent missing values:")
    print(df.isnull().sum())

    print("\nChoose option:")
    print("1. Drop rows with missing values")
    print("2. Fill numeric with MEAN")
    print("3. Fill numeric with MEDIAN")
    print("4. Fill categorical with MODE")
    print("5. Fill ALL (num=median, cat=mode)")
    print("6. Drop a column completely")

    ch = input("Enter choice: ")

    if ch == "1":
        df = df.dropna()
        print("Rows dropped.")

    elif ch == "2":
        for c in df.select_dtypes(include="number"):
            df[c].fillna(df[c].mean(), inplace=True)
        print("Numeric columns filled with mean.")

    elif ch == "3":
        for c in df.select_dtypes(include="number"):
            df[c].fillna(df[c].median(), inplace=True)
        print("Numeric columns filled with median.")

    elif ch == "4":
        for c in df.select_dtypes(include="object"):
            df[c].fillna(df[c].mode()[0], inplace=True)
        print("Categorical columns filled with mode.")

    elif ch == "5":
        for c in df.select_dtypes(include="number"):
            df[c].fillna(df[c].median(), inplace=True)
        for c in df.select_dtypes(include="object"):
            df[c].fillna(df[c].mode()[0], inplace=True)
        print("All missing values handled.")

    elif ch == "6":
        print("\nAvailable Columns:")
        print(list(df.columns))

        col = input("Enter column name to DROP: ")
        if col in df.columns:
            df.drop(columns=[col], inplace=True)
            print(f"Column '{col}' dropped.")
        else:
            print("Column not found!")

    else:
        print("Invalid choice!")

    print("\nUpdated missing values:")
    print(df.isnull().sum())
    return df


def visualization_menu(df):
    print("\nAvailable Columns:")
    print(list(df.columns))

    print("\nChoose chart type:")
    print("1. Line Plot")
    print("2. Bar Plot")
    print("3. Scatter Plot")
    print("4. Box Plot")
    print("5. Violin Plot")
    print("6. Histogram")
    print("7. Pie Chart")

    ch = input("Enter choice: ")
    plt.figure(figsize=(9,5))

    try:
        if ch in ["1", "2", "3", "4", "5"]:
            x = input("Enter X column: ")
            y = input("Enter Y column: ")
            hue = input("Enter Hue column (Enter to skip): ")
            hue = hue if hue != "" else None

            if ch == "1":
                sns.lineplot(x=x, y=y, hue=hue, data=df, palette="Set2")
                plt.savefig("lineplot.png", dpi=300, bbox_inches='tight')
            elif ch == "2":
                sns.barplot(x=x, y=y, hue=hue, data=df, palette="Set2")
                plt.savefig("barplot.png", dpi=300, bbox_inches='tight')
            elif ch == "3":
                sns.scatterplot(x=x, y=y, hue=hue, data=df, palette="Set2")
                plt.savefig("scatterplot.png", dpi=300, bbox_inches='tight')
            elif ch == "4":
                sns.boxplot(x=x, y=y, hue=hue, data=df, palette="Set2")
                plt.savefig("boxplot.png", dpi=300, bbox_inches='tight')
            elif ch == "5":
                sns.violinplot(x=x, y=y, hue=hue, data=df, palette="Set2")
                plt.savefig("violinplot.png", dpi=300, bbox_inches='tight')

            plt.title(f"{y} vs {x}", fontweight="bold", fontsize=14)

        elif ch == "6":
            x = input("Enter column for Histogram: ")
            sns.histplot(df[x], kde=True, color="#532082")
            plt.title(f"Distribution of {x}", fontweight="bold")
            plt.savefig("histogram.png", dpi=300, bbox_inches='tight')

        elif ch == "7":
            col = input("Enter column for Pie Chart: ")
            df[col].value_counts().plot.pie(autopct="%1.1f%%", colors=sns.color_palette("Set2"),
                                            startangle=90, shadow=True)
            plt.title(f"{col} Distribution", fontweight="bold")
            plt.savefig("piechart.png", dpi=300, bbox_inches='tight')

        else:
            print("Invalid chart choice!")
            return

        plt.show()

    except Exception as e:
        print("Plotting error:", e)


def main():
    df = load_dataset()
    if df is None:
        print("Program exited.")
        return

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Dataset Information")
        print("2. Handle Missing Values")
        print("3. Data Visualization")
        print("0. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            dataset_info_menu(df)
        elif ch == "2":
            df = handle_missing_values(df)
        elif ch == "3":
            visualization_menu(df)
        elif ch == "0":
            print("\nThank you! Program ended.")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
