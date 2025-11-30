import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['Date'])
    df.dropna(inplace=True)
    return df

def basic_stats(df):
    print("Basic Statistics:")
    print(df.describe())

def sales_over_time(df):
    daily_sales = df.groupby('Date')['Revenue'].sum().reset_index()
    plt.figure(figsize=(10,5))
    sns.lineplot(data=daily_sales, x='Date', y='Revenue')
    plt.title("Total Revenue Over Time")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

def revenue_by_product(df):
    product_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
    plt.figure(figsize=(8,5))
    sns.barplot(x=product_revenue.values, y=product_revenue.index, palette='viridis')
    plt.title("Total Revenue by Product")
    plt.xlabel("Revenue")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.show()

def revenue_distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df['Revenue'], bins=20, kde=True)
    plt.title("Distribution of Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

def quantity_vs_revenue(df):
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=df, x='Quantity_Sold', y='Revenue', hue='Product')
    plt.title("Quantity Sold vs Revenue")
    plt.xlabel("Quantity Sold")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    filepath = 'farm_sales.csv'
    df = load_and_clean_data(filepath)
    basic_stats(df)
    sales_over_time(df)
    revenue_by_product(df)
    revenue_distribution(df)
    quantity_vs_revenue(df)
