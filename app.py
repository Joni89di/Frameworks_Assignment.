import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Mwena Agritech: Farm Sales Dashboard")
st.write("Upload your farm sales CSV to explore your product performance.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])
    st.write("### Sample Data")
    st.dataframe(df.head())

    # Sidebar filters
    st.sidebar.header("Filter Options")
    min_date = df['Date'].min()
    max_date = df['Date'].max()

    date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])
    product_options = df['Product'].unique().tolist()
    selected_products = st.sidebar.multiselect("Select Products", product_options, default=product_options)

    # Filter data
    filtered_df = df[
        (df['Date'] >= pd.to_datetime(date_range[0])) &
        (df['Date'] <= pd.to_datetime(date_range[1])) &
        (df['Product'].isin(selected_products))
    ]

    st.write(f"### Showing data from {date_range[0]} to {date_range[1]} for products: {', '.join(selected_products)}")

    if not filtered_df.empty:
        # Total revenue over time
        revenue_time = filtered_df.groupby('Date')['Revenue'].sum().reset_index()
        fig, ax = plt.subplots()
        sns.lineplot(data=revenue_time, x='Date', y='Revenue', ax=ax)
        ax.set_title("Total Revenue Over Time")
        st.pyplot(fig)

        # Revenue by product
        revenue_product = filtered_df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
        fig, ax = plt.subplots()
        sns.barplot(x=revenue_product.values, y=revenue_product.index, ax=ax, palette='coolwarm')
        ax.set_title("Total Revenue by Product")
        st.pyplot(fig)

        # Revenue distribution histogram
        fig, ax = plt.subplots()
        sns.histplot(filtered_df['Revenue'], bins=20, kde=True, ax=ax)
        ax.set_title("Revenue Distribution")
        st.pyplot(fig)

        # Quantity vs revenue scatter
        fig, ax = plt.subplots()
        sns.scatterplot(data=filtered_df, x='Quantity_Sold', y='Revenue', hue='Product', ax=ax)
        ax.set_title("Quantity Sold vs Revenue")
        st.pyplot(fig)
    else:
        st.warning("No data available for selected filters.")
else:
    st.info("Upload a CSV file to begin.")
