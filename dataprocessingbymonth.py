import pandas as pd
import os

column_names = [
    "LOAN_SEQUENCE_NUMBER", "MONTHLY_REPORTING_PERIOD", "CURRENT_ACTUAL_UPB", "CURRENT_LOAN_DELINQUENCY_STATUS",
    "LOAN_AGE", "REMAINING_MONTHS", "REPURCHASE_FLAG", "MODIFICATION_FLAG", "ZERO_BALANCE_CODE",
    "ZERO_BALANCE_EFFECTIVE_DATE", "CURRENT_INTEREST_RATE", "CURRENT_DEFERRED_UPB", "DUE_DATE_OF_LAST_PAID_INSTALLMENT",
    "MI_RECOVERIES", "NET_SALES_PROCEEDS", "NON_MI_RECOVERIES", "EXPENSES", "LEGAL_COSTS", "MAINTENANCE_AND_PRESERVATION_COSTS",
    "TAXES_AND_INSURANCE", "MISCELLANEOUS_EXPENSES", "ACTUAL_LOSS_CALCULATION", "MODIFICATION_COST", "STEP_MODIFICATION_FLAG",
    "DEFERRED_PAYMENT_MODIFICATION", "ESTIMATED_LOAN_TO_VALUE", "ZERO_BALANCE_REMOVAL_UPB", "DELINQUENT_ACCRUED_INTEREST",
    "DELINQUENCY_DUE_TO_DISASTER", "BORROWER_ASSISTANCE_STATUS_CODE", "CURRENT_MONTH_LIQUIDATION_FLAG", "CURRENT_MONTH_REPURCHASE_FLAG"
]


for year in range(2006, 2024):  # 2024 because the range end is exclusive
    print(year)
    file_path1 = f'hist_time_parquet/hist_data_time_{year}Q1.parquet'
    df1 = pd.read_parquet(file_path1)
    
     
    file_path2 = f'hist_time_parquet/hist_data_time_{year}Q2.parquet'
    df2 = pd.read_parquet(file_path2)
    
    file_path3 = f'hist_time_parquet/hist_data_time_{year}Q3.parquet'
    df3 = pd.read_parquet(file_path3)
    
    file_path4 = f'hist_time_parquet/hist_data_time_{year}Q4.parquet'
    df4 = pd.read_parquet(file_path4)
    

    df1.columns = column_names
    df2.columns = column_names
    df3.columns = column_names
    df4.columns = column_names

    big_df = pd.concat([df1, df2, df3, df4], axis=0, ignore_index=True)

    
    #sort the big dataframe by months
    directory = 'hist_time_by_month'
    #append a file for each months column in this step here
    # Iterate over each group
    for name, group in big_df.groupby('MONTHLY_REPORTING_PERIOD'):
        file_path = os.path.join(directory, f'{name}.parquet')
        
        if os.path.exists(file_path):
            # Read the existing data
            existing_data = pd.read_parquet(file_path)
            
            # Concatenate the new data
            updated_data = pd.concat([existing_data, group], ignore_index=True)
        else:
            updated_data = group
        
        # Write (or overwrite) the Parquet file
        updated_data.to_parquet(file_path, engine='pyarrow', index=False)
    