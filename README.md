### Summary of the Project: "Prepayment Risk"

**Authors:** Y. Fan, T. Fan, X. Liu & J. Gruber  
**Institution:** Baruch College MFE  
**Date:** August 26, 2024

This project, titled "Prepayment Risk," focuses on analyzing and predicting the risk of prepayment in mortgage loans using various data analysis and machine learning techniques. The project is divided into two main tasks, each tackling different aspects of prepayment prediction.

### Key Sections and Findings:

1. **Exploratory Data Analysis (EDA):**
   - The EDA aimed to understand the patterns of prepayment over time, identifying that most prepayments occur after 7 years. This insight was used to define a cutoff period for data analysis.
   - The relationship between interest rate changes and prepayment rates was also explored, showing a correlation between lower interest rates and higher prepayment rates.

2. **Problem Definition:**
   - **Problem 1:** Given a loan profile at the origination, predict whether there will ever be a prepayment. This approach requires a smaller dataset and focuses on understanding long-term prepayment risk using survival analysis.
   - **Problem 2:** Given a loan at a specific time, predict the probability of prepayment in the next period. This problem is more dynamic and potentially more applicable in industry settings, focusing on short-term prediction.

3. **Data Processing:**
   - **Handling Missing Data:** Missing critical variables (like FICO score, CLTV, LTV) led to the exclusion of certain samples, while other missing data points were handled using median/mode imputations and indicator variables.
   - **Feature Engineering:** Categorical variables were converted into dummy variables for certain models, and macroeconomic features like mortgage rates and unemployment rates were added to enhance prediction accuracy.

4. **Modeling Approach for Problem 1:**
   - **Machine Learning Models:** The team used Boosting Trees (LightGBM) and Neural Networks. LightGBM was chosen for its robustness to missing values and categorical features, while Neural Networks were selected for their ability to handle non-linearity and interaction effects.
   - **Results:** Both models showed good predictive capabilities, with notable metrics like accuracy, ROC curves, and precision-recall, though some overfitting was observed.

5. **Problem 2 - Data Preparation and Technical Considerations:**
   - The team encountered challenges with data handling and model training due to memory constraints. They compared tools like Polars vs. Pandas for data processing and evaluated storage formats (Parquet, CSV, TXT), finding Parquet most suitable for large datasets.
   - **Challenges:** The project faced unresolved memory errors when processing large datasets, leading to incomplete analysis in Task 2. Proposed solutions included using more powerful computing resources or integrating a database system for better data management.

6. **Conclusion:**
   - The project successfully demonstrated the ability to predict mortgage prepayment risk using machine learning models, especially over a four-year period. However, technical challenges in data handling and model training suggest that future work could benefit from enhanced computational resources or a more optimized data infrastructure.

### Technical Tools Used:
- **Programming and Libraries:** Python, using Pandas and Polars for data processing, and LightGBM for machine learning.
- **Data Storage:** The team experimented with Parquet, CSV, and TXT formats, ultimately favoring Parquet for its efficiency with large datasets.
- **Machine Learning:** LightGBM was the primary model for tree-based predictions, while a custom Neural Network architecture was used for deep learning tasks.

### Summary of the Project:
The project provides a comprehensive approach to understanding and predicting prepayment risk in mortgage loans, leveraging both exploratory data analysis and advanced machine learning models. Despite some technical challenges, the results highlight significant predictive capabilities, with potential applications in the finance industry. The use of cutting-edge tools like LightGBM and Neural Networks, combined with a thoughtful approach to data processing, underscores the project's practical relevance and innovation.
