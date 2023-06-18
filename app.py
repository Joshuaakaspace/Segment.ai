import streamlit as st
import pandas as pd

def search_names(search_entry):
    df = pd.read_csv('companies_sorted.csv')
    df['name'] = df['name'].fillna('')
    results = df[df['name'].str.startswith(search_entry)]
    return results

def main():
    st.title("Name Search App")
    
    csv_file = 'your_file.csv'  # Replace with your CSV file path
    search_entry = st.text_input("Enter the starting letters for name search:")
    
    if st.button("Search"):
        results = search_names( search_entry)
        st.table(results)

if __name__ == '__main__':
    main()
