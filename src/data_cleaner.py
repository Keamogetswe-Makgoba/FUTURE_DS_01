import pandas as pd
import numpy as np

def clean_sales_data(df):
    """
    Performs advanced data cleaning: duplicates, null imputation, and outlier removal.
    """
    # 1. Now we remove duplicates
   
    original_count = len(df)
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset=['order_id', 'product_id'], keep='first')
    print(f"Removed {original_count - len(df)} duplicate rows.")

    # 2. Handling nulls (Imputation)
  
    categorical_cols = ['segment', 'region', 'category', 'sub_category']
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown')

    # 3.Outlier detection(IQR)
    
    Q1 = df['sales'].quantile(0.25)
    Q3 = df['sales'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filtering to keep only normal range sales
    df = df[(df['sales'] >= lower_bound) & (df['sales'] <= upper_bound)]
    print(f"Filtered outliers. Final row count: {len(df)}.")

    # 4. Now we do the integrity check
    df = df[df['sales'] > 0]
    
    return df