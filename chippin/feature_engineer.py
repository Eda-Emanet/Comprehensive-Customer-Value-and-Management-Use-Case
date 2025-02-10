import pandas as pd

class FeatureEngineer:
    def __init__(self, df: pd.DataFrame):
        """
        feauture  eklemek ve duzenlemek icin;
        """
        self.df = df

    def add_feature_columns(self) -> pd.DataFrame:
       
        # Branch count per customer
        self.df['branch_count'] = self.df.groupby('unique_customer_id')['cb_branch_id'].transform('nunique')
        
        # Total discount per customer
        self.df['discount_sum'] = self.df.groupby('unique_customer_id')['amount_discount'].transform('sum')
        
        # Total pre-discount spending per customer
        self.df['Monetary_beforeDis'] = self.df.groupby('unique_customer_id')['amount_before_discount'].transform('sum')
        
        return self.df

    def add_additional_features(self, rfm: pd.DataFrame) -> pd.DataFrame:
        """RFM data ile birlestirmek icin"""
        df = pd.merge(self.df, rfm, on='unique_customer_id', how='left')

        df['avg_amount_spent'] = df['Monetary'] / df['Frequency']
        df['avg_discount'] = df['discount_sum'] / df['Frequency']
        df["discount_rate"] = df['discount_sum'] / df['Monetary_beforeDis']
        df["discount_per_branch"] = df['discount_sum'] / df['branch_count']
        df["Monetary_branch"] = df['discount_sum'] / df['branch_count']
        df['branch_discount_interaction'] = df['branch_count'] * df['discount_rate']
        df['spend_ratio'] = df['Monetary'] / df['Monetary_beforeDis']
        df['discount_impact'] = 1 - df['spend_ratio']

        # tekrarlayan satirlari silmek icin 
        data_new = df[['branch_count', 'discount_sum', 'Recency', 'Frequency',
                       'unique_customer_id', 'discount_rate', 'discount_per_branch',
                       'Monetary_beforeDis', 'Monetary', 'avg_amount_spent', 'avg_discount', 
                       'Monetary_branch', 'branch_discount_interaction', 'RF_segment',
                       'spend_ratio', 'discount_impact']]
        data_new.drop_duplicates(inplace=True)
        return data_new