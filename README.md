# Comprehensive Customer Value and Management Use Case

Overview;

 In this study, the given datasets were examined and the CLV and Churn prediction model was established and then dockerized.
 Given columns;

   - `unique_customer_id`:The unique identifier of the customer.
   - `gender`: The gender of the customer.
   - `date_of_birth`: The date of birth of the customer (Some values may be missing).
   - `cb_customer_id`: The identifier of the customer in another system.
   - `transaction_date`: The date of the transaction.
   - `amount_after_discount`: The transaction amount after discount (Values may have been transformed).
   - `cb_branch_id`: The identifier of the branch where the transaction took place.
   - `amount_before_discount`: The transaction amount before discount (Values may have been transformed).
   - `amount_discount`: The discount amount applied (Values may have been transformed).
Data has been loaded and cleared.
Since the dataset provided for the churn model does not include any churn label, the churn segment created using the RF score was selected as the target variable.
- As success metrics, due to the slight imbalance in the dataset, both F1 macro (which gives more weight to the minority class) and Accuracy were observed.
- The best model turned out to be an XGBoost model, achieving 0.71 Accuracy and 0.69 F1 Macro score.
- Hyperparameter optimization was attempted, but it did not improve the score.

- In the CLV Prediction study, the monetary variable will be predicted using regression analysis.
- The monetary variable is defined as the sum of individuals' amount_after_discount values.
-  Due to the possibility that the monetary variable is scaled, the success metric was chosen as the Adjusted R².
-  Adjusted R² score was found to be 0.817. (RMSE 0.43)


- All studies and class structure have been added to this repository and you can find the presentation in the CustomerValue file.

  # Docker

- Pull it with docker **pull edaemanet/my-app**
 - You can run it with docker **run -p 8888:8888 edaemanet/my-app** and access it from localhost:8888.


 

Docker kullanmak için; docker pull edaemanet/my-app ile çekip docker run -p 8888:8888 edaemanet/my-app  ile çalıştırıp localhost:8888'den ulaşabilirsiniz.
