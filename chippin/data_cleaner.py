import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        """
        Data temizligi icin

        """
        self.df = df

    def clean_gender_data(self) -> pd.DataFrame:
        """  NaN"""
        self.df['gender'] = self.df['gender'].replace('UNKNOWN', np.nan)
        return self.df

    def convert_date_columns(self) -> pd.DataFrame:
       
        self.df['transaction_date'] = pd.to_datetime(self.df['transaction_date'])
        self.df['date_of_birth'] = pd.to_datetime(self.df['date_of_birth'])
        return self.df

    def drop_unnecessary_columns(self) -> pd.DataFrame:
        
        self.df.drop(columns=['date_of_birth', 'gender'], inplace=True)
        return self.df