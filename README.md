# Comprehensive Customer Value and Management Use Case

Overview;
 In this study, the data sets given were analyzed and CLV and Churn prediction models were established and dockerized.
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
     
# Structure
- Data has been loaded and cleared.
- Variables were examined and missing values ​​and outlier values ​​were examined.
- The correlations and distributions of the variables were examined.
- New variables have been created.
- RFM metrics have been added.
- Churn and CLV models have been established.
- The success of the models has been tried to be increased by hyperparameter optimization.
- The entire structure has been dockerized and Docker image sent to Dockerhub.
- CustomerValue python file prepared for presentation, class structures prepared for data cleaning, loading, feature engineering, training of CLV and Churn models, Dockerfile and requirements.txt file
  has been added to this repository. 


# Churn Predict 
Since the dataset provided for the churn model does not include any churn label, the churn segment created using the RF score was selected as the target variable.
- As success metrics, due to the slight imbalance in the dataset, both F1 macro (which gives more weight to the minority class) and Accuracy were observed.
- The best model turned out to be an XGBoost model, achieving 0.71 Accuracy and 0.69 F1 Macro score.
- Hyperparameter optimization was attempted, but it did not improve the score.

# CLV Predict
- In the CLV Prediction study, the monetary variable will be predicted using regression analysis.
- The monetary variable is defined as the sum of individuals' amount_after_discount values.
-  Due to the possibility that the monetary variable is scaled, the success metric was chosen as the Adjusted R².
-  Adjusted R² score was found to be 0.817. (RMSE 0.43)

  # Docker

- Pull it with **docker pull edaemanet/my-app**
- You can run it with **docker run -p 8888:8888 edaemanet/my-app** and access it from localhost:8888.

