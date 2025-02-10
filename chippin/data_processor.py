import pandas as pd
from data_loader import DataLoader
from data_cleaner import DataCleaner
from feature_engineer import FeatureEngineer
from rfm_calculator import RFMCalculator

class DataProcessor:
    def __init__(self, best_path: str, cust_path: str, trx_path: str):
        """
        Tum yapıyı bir araya getirmek icin
        """
        self.loader = DataLoader(best_path, cust_path, trx_path)
        self.df = None
        self.data = None
        self.rfm = None

    def process_data(self) -> pd.DataFrame:
        """pipeline"""
        best, cust, trx = self.loader.load_data()
        
        # datayi birlestir
        merged_trx = pd.merge(trx, cust, on='cb_customer_id', how='inner')
        self.df = pd.merge(merged_trx, best, on='unique_customer_id', how='left')
        self.df.drop_duplicates(inplace=True)
        
        # Temizlemek icin
        cleaner = DataCleaner(self.df)
        cleaner.clean_gender_data()
        cleaner.convert_date_columns()
        cleaner.drop_unnecessary_columns()
        
        # Degisken muhendisligi
        engineer = FeatureEngineer(self.df)
        engineer.add_feature_columns()
        
        # Calculate RFM
        rfm_calculator = RFMCalculator(self.df)
        self.rfm = rfm_calculator.calculate_rfm()
        rfm_calculator.assign_rfm_scores()
        
        # ek degiskenler 
        self.data = engineer.add_additional_features(self.rfm)
        return self.data

    def get_processed_data(self) -> pd.DataFrame:
        """Data"""
        if self.data is None:
            raise ValueError("Data has not been processed yet. Run process_data() first.")
        return self.data

    def get_rfm_data(self) -> pd.DataFrame:
        """RFM datasi."""
        if self.rfm is None:
            raise ValueError("Data has not been processed yet. Run process_data() first.")
        return self.rfm