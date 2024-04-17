import io
import pandas as pd
import requests
import faostat

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    
    df = faostat.get_data_df('QCL',
    pars={'element':[2312],'item':'15'}, 
    show_flags=False, null_values=False, https_proxy=None)

    df["Domain Code"] = df['Domain Code'].astype('str')
    df["Domain"] = df['Domain'].astype('str')
    df["Area Code"] = df['Area Code (FAO)'].astype('int64')
    df["Area"] = df['Area'].astype('str')
    df["Element Code"] = df['Element Code'].astype('int')
    df["Element"] = df['Element'].astype('str')
    df["Item Code"] = df['Item Code'].astype('int64')
    df["Item"] = df['Item'].astype('str')
    df["Year Code"] = df['Year Code'].astype('int')
    df["Year"] = pd.to_datetime(df['Year'], format='%Y')
    df["Unit"] = df['Unit'].astype('str')
    df["Value"] = df['Value'].astype('int64')
    df["Note"] = df['Note'].astype('str')   
    
    #df = df[['Domain Code', 'Area', 'Item', 'Year', 'Unit', 'Value']]

    df = df[['Domain Code', 'Area', 'Item', 'Year','Value']]
    
    

    return df
