import pandas as pd
import streamlit as st

def main():
    # Load your actual data file
    df = pd.read_csv(r"C:\Users\dhivy\OneDrive\Desktop\HTML tutorial\ESS\co2_emissions_kt_by_country.csv")  # Update this if your file is in a different location

    # Example: Display the data
    st.title("CSV Data Viewer")
    st.write(df)

if __name__ == "__main__":
    main()
