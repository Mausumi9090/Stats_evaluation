import openpyxl
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import openpyxl

def main():
    st.title("This is my ecommerce app i am creating")
    st.sidebar.title("you can upload your  file here ")
    upload_file=st.sidebar.file_uploader("Upload your file",type=["csv","xlsx"])
    if upload_file is not None:
        try:
            if upload_file.name.endswith('csv'):
                data = pd.read_csv(upload_file)
            else:
                data = pd.read_excel(upload_file)
            st.sidebar.success('Your file has been uploaded')
            st.subheader('i am going to show you a data details')
            st.subheader("lets see some more details in data")
            st.write("shape of the data ", data.shape)
            st.write("the column name inside datails data is ",data.columns)
            st.write("the missing value into column",data.isnull().sum())
            st.dataframe(data.head())
            st.subheader("i will show you a bit of stats")
            st.write(data.describe())
        except Exception as e:
            print(e)

if __name__== "__main__":

    main()
