import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor

class CLVModel:
    def __init__(self, data: pd.DataFrame, seed: int = 42):
        """
        CLV için değişken ve model seçimi / test-train ayırımı/ model eğitimi ve doğruluk skoruna bakma aşamalarını içerir.
        """
        self.data = data
        self.seed = seed
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        self.model = RandomForestRegressor(n_estimators=100, random_state=self.seed)

    def prepare_data(self) -> None:
 
        features = ["Recency", 'Frequency', 'avg_discount', 'branch_count']
        x = self.data[features]
        y = self.data["Monetary"]

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            x, y, test_size=0.2, random_state=self.seed, shuffle=True
        )

    def train_model(self) -> None:
        
         self.model.fit(self.x_train, self.y_train)

    def evaluate_model(self) -> None:

        
        y_pred = self.model.predict(self.x_test)
        mse = mean_squared_error(self.y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(self.y_test, y_pred)

        n = len(self.y_test)
        p = self.x_test.shape[1]
        adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

        print("Test RMSE:", rmse)
        print("Test R^2 Score:", r2)
        print("Test Adjusted R^2 Score:", adjusted_r2)

    def run(self) -> None:
        self.prepare_data()
        self.train_model()
        self.evaluate_model()

