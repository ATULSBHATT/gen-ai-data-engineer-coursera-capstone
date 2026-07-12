# IBM Coursera Capstone: Generative AI for Data Engineers

This repository contains my final capstone project for the **Generative AI for Data Engineers Specialization** by IBM on Coursera. 

As an experienced data professional, I designed this project to showcase how Generative AI can be used to accelerate enterprise data architecture, enforce data quality, and build secure ETL pipelines.

## 🛠️ Project Scope
1. **AI-Driven Architecture:** Leveraged LLMs to design an optimized Star Schema for an e-commerce data warehouse.
2. **Prompt Engineering:** Utilized Chain-of-Thought and Constraint-based prompting to generate high-quality synthetic datasets and transformation logic.
3. **Secure ETL Pipeline:** Built a Python/Pandas data pipeline that cleanses raw data, standardizes formats, and strictly masks Personally Identifiable Information (PII) using SHA256 hashing before loading it into a target Parquet file.

## 📁 Repository Structure
* `1_ai_prompts_log.md`: Documentation of the prompt engineering techniques used.
* `2_warehouse_schema.sql`: The finalized DDL statements for the Data Warehouse.
* `3_etl_pipeline.py`: The execution script for data extraction, transformation, and secure loading.

## 🚀 How to Run
```bash
pip install pandas pyarrow
python 3_etl_pipeline.py
