import pandas as pd

class DataLoader:
    def __init__(self, best_path: str, cust_path: str, trx_path: str):
        """
        Csv dosyalarını eklemek icin
        """
        self.best_path = best_path
        self.cust_path = cust_path
        self.trx_path = trx_path

    def load_data(self) -> tuple:
        """csv"""
        best = pd.read_csv(self.best_path)
        cust = pd.read_csv(self.cust_path)
        trx = pd.read_csv(self.trx_path)
        return best, cust, trx