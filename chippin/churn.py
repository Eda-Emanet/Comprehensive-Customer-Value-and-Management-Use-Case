import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier
import warnings
warnings.filterwarnings("ignore")

class ChurnModel:
    def __init__(self, data: pd.DataFrame, seed: int = 42):
        """
        Churn modeli için gerekli kolon seçimi, test-train ayırımı, model seçimi gibi 
        işlemleri yapar.
        """
        self.data = data
        self.seed = seed
        self.pipeline = Pipeline([
            #('scaler', StandardScaler()), 
            ('model', XGBClassifier(random_state=self.seed))  
        ])
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None

    def prepare_data(self) -> None:
        self.data['churn_flag'] = np.where(self.data['RF_segment'] == "Churn", 1, 0)

        data_new = self.data[['branch_count', 'discount_sum', 'Recency', 'Frequency',
                              'unique_customer_id', 'discount_rate', 'discount_per_branch',
                              'Monetary_beforeDis', 'Monetary', 'avg_amount_spent', 'avg_discount', 
                              'churn_flag', 'Monetary_branch', 'branch_discount_interaction', 
                              'spend_ratio', 'discount_impact']]
        data_new.drop_duplicates(inplace=True)

        x = data_new[[  'branch_count', 'Monetary_beforeDis', 'avg_discount',   'discount_impact']]
        y = data_new[['churn_flag']]

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            x, y, test_size=0.2, random_state=self.seed, stratify=y, shuffle=True
        )

    def train_model(self) -> None:
        self.pipeline.fit(self.x_train, self.y_train)

    def evaluate_model(self) -> None:
        y_pred = self.pipeline.predict(self.x_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        print("Test Seti Doğruluk Skoru:", accuracy)
        print("\nSınıflandırma Raporu:")
        print(classification_report(self.y_test, y_pred))

    def run(self) -> None:
        self.prepare_data()
        self.train_model()
        self.evaluate_model()