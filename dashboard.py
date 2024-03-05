import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to plot bar graph
def plot_bar_graph(data, x_column, y_column):
    st.subheader("Bar Graph")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x=x_column, y=y_column)
    st.pyplot()

# Function to plot pie chart
def plot_pie_chart(data, x_column, y_column):
    st.subheader("Pie Chart")
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(data[y_column], labels=data[x_column], autopct='%1.1f%%')
    st.write(fig)
    st.pyplot()

# Function to plot scatter plot
def plot_scatter_plot(data, x_column, y_column):
    st.subheader("Scatter Plot")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_column, y=y_column)
    st.pyplot()

# Main function
def main():
    st.title("Excel File Analysis Dashboard")

    # File upload
    uploaded_file = st.file_uploader("Upload Excel file", type=["xls", "xlsx"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)

        # Display data
        st.subheader("Data")
        st.write(df)

        # Choose type of plot
        plot_type = st.selectbox("Select type of plot", ["Bar Graph", "Pie Chart", "Scatter Plot"])

        if plot_type in ["Bar Graph", "Pie Chart", "Scatter Plot"]:
            # Select columns for X and Y axes
            x_column = st.selectbox("Select X-axis column", df.columns)
            y_column = st.selectbox("Select Y-axis column", df.columns)

            if plot_type == "Bar Graph":
                plot_bar_graph(df, x_column, y_column)
            elif plot_type == "Pie Chart":
                plot_pie_chart(df, x_column, y_column)
            elif plot_type == "Scatter Plot":
                plot_scatter_plot(df, x_column, y_column)

if __name__ == "__main__":
    main()
