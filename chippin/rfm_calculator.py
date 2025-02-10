import pandas as pd
import numpy as np

class RFMCalculator:
    def __init__(self, df: pd.DataFrame):
        """
        RFM metriklerini hesaplamak icin
        """
        self.df = df
        self.rfm = None

    def calculate_rfm(self) -> pd.DataFrame:
        """RFM (Recency, Frequency, Monetary) metrikleri"""
        max_date = self.df['transaction_date'].max()

        #  Recency
        rfm_data = self.df.groupby('unique_customer_id').agg({
            'transaction_date': lambda x: x.max(),
        })
        rfm_data['Recency'] = (max_date - rfm_data['transaction_date']).dt.days
        rfm_data.drop(columns='transaction_date', inplace=True)

        #  Frequency
        freq_data = self.df.groupby('unique_customer_id').agg({
            'transaction_date': 'count'
        }).rename(columns={'transaction_date': 'Frequency'})

        # Monetary
        mon_data = self.df.groupby('unique_customer_id').agg({
            'amount_after_discount': 'sum'
        }).rename(columns={'amount_after_discount': 'Monetary'})

        # Tum metrikler
        self.rfm = rfm_data.join(freq_data).join(mon_data)
        return self.rfm

    def assign_rfm_scores(self) -> pd.DataFrame:
        """RFM skoru ve segmenti atama """
        if self.rfm is None:
            raise ValueError("RFM metrics must be calculated first")

        # Recency scoring
        self.rfm['R_Score'] = pd.qcut(self.rfm['Recency'], 5, labels=[5,4,3,2,1])
        
        # Frequency scoring
        bins = [0, 1, 2, 3, 5, np.inf]
        labels = [1, 2, 3, 4, 5]
        self.rfm['F_Score'] = pd.cut(self.rfm['Frequency'], bins=bins, labels=labels)
        
        # Monetary scoring
        self.rfm['M_Score'] = pd.qcut(self.rfm['Monetary'], 5, labels=[1,2,3,4,5])
        
        # Combined RF score
        self.rfm['RF_Score'] = self.rfm['R_Score'].astype(str) + self.rfm['F_Score'].astype(str)

        # Segment mapping
        seg_map = {
            r'[1-2][1-2]': 'Churn',
            r'[1-2][3-4]': 'at_Risk',
            r'[1-2]5': 'cant_loose',
            r'3[1-2]': 'about_to_sleep',
            r'33': 'need_attention',
            r'[3-4][4-5]': 'loyal_customers',
            r'41': 'promising',
            r'51': 'new_customers',
            r'[4-5][2-3]': 'potential_loyalists',
            r'5[4-5]': 'champions'
        }
        
        self.rfm['RF_segment'] = self.rfm['RF_Score'].replace(seg_map, regex=True)
        return self.rfm