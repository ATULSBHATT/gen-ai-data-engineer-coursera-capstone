# Generative AI Prompt Engineering Log

As part of this capstone, Generative AI (LLMs) were used to accelerate the architecture and ETL pipeline design. Below are the structured prompts used to generate the infrastructure.

### Task 1: Schema Architecture Generation
**Prompt Strategy Used:** Role-Playing & Few-Shot Prompting
> "Act as a Lead Enterprise Data Architect. I am migrating legacy e-commerce flat files to a Snowflake data warehouse. Design a Star Schema with 1 Fact table (Sales) and 3 Dimension tables (Users, Products, Time). Provide the ANSI SQL DDL statements with appropriate primary/foreign keys and standard data types."

### Task 2: Synthetic Data Generation for Testing
**Prompt Strategy Used:** Constraint-Based Prompting
> "Generate 10 rows of synthetic mock data for the 'Users' dimension table. The output must be valid CSV format. Columns: user_id, first_name, last_name, email, registration_date. Ensure 2 of the emails are intentionally malformed to test my ETL error handling."

### Task 3: ETL Transformation Logic
**Prompt Strategy Used:** Step-by-Step Chain of Thought
> "Act as a Data Engineer. Write a Python pandas script to read the synthetic Users CSV. Perform the following transformations: 1. Drop rows with null emails. 2. Standardize all first names to title case. 3. Mask the email column using SHA256 hashing for PII compliance. Output the final dataframe to a parquet file."
