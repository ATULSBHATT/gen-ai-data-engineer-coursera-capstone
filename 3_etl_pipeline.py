import pandas as pd
import hashlib
import os

def mask_pii(text: str) -> str:
    """Uses SHA256 to mask PII data (Emails/Names) as recommended by the AI Architect."""
    if pd.isna(text):
        return text
    return hashlib.sha256(str(text).encode('utf-8')).hexdigest()

def run_etl_pipeline():
    print("🚀 Starting Capstone ETL Pipeline...")
    
    # 1. EXTRACT: Create synthetic raw data (Usually generated via Gen AI for the capstone)
    print("📥 Extracting raw legacy data...")
    raw_data = {
        "user_id": [1, 2, 3],
        "first_name": ["john", "JANE", "alice"],
        "email": ["john@email.com", "jane@corp.com", None],
        "registration_date": ["2026-01-15", "2026-03-20", "2026-04-05"]
    }
    df = pd.DataFrame(raw_data)
    
    # 2. TRANSFORM: Apply AI-suggested business logic
    print("⚙️ Applying data quality transformations & PII masking...")
    
    # Drop invalid records
    df = df.dropna(subset=['email'])
    
    # Standardize formats
    df['first_name'] = df['first_name'].str.title()
    df['registration_date'] = pd.to_datetime(df['registration_date'])
    
    # Mask Sensitive Data
    df['email_hash'] = df['email'].apply(mask_pii)
    df = df.drop(columns=['email']) # Drop raw email to secure pipeline
    
    # 3. LOAD: Save to analytics-ready format
    print("📤 Loading clean data to target directory...")
    os.makedirs('output', exist_ok=True)
    target_path = 'output/dim_users_clean.parquet'
    
    # Save as Parquet (Standard enterprise format, much better than CSV)
    df.to_parquet(target_path, index=False)
    
    print(f"✅ Pipeline complete! Clean data loaded to {target_path}")
    print("\nPreview of processed data:")
    print(df.head())

if __name__ == "__main__":
    run_etl_pipeline()
