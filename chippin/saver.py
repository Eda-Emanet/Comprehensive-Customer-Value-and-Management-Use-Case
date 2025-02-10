import os
import joblib

class ModelSaver:
    def __init__(self, save_dir='models'):
        self.save_dir = save_dir
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def save_model(self, model, model_name):
        """
       Modeli kaydetmek icin;
        """
        model_path = os.path.join(self.save_dir, f"{model_name}.pkl")
        joblib.dump(model, model_path)
        print(f"Model saved to {model_path}")

    def load_model(self, model_name):
        """
        Modeli yuklemek icin;
        """
        model_path = os.path.join(self.save_dir, f"{model_name}.pkl")
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            print(f"Model loaded from {model_path}")
            return model
        else:
            raise FileNotFoundError(f"No model found at {model_path}")