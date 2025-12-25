# ETL Pipeline & Data Quality Checks
Structured ETL pipeline with data quality validation using Python and Pandas.

## Features
- Extracts and validates CSV data
- Enforces schema and type validation
- Creates missingness reports
- Normalizes text data
- Adds missing value flags
- Exports to Parquet format
- Generates logging output

## Project Structure
```
.
├── data
│   ├── cache
│   ├── external
│   ├── processed
│   │   ├── orders.parquet
│   │   ├── orders_clean.parquet
│   │   └── users.parquet
│   └── raw
│       ├── orders.csv
│       └── users.csv
├── images
│   ├── processed_day1.png
│   ├── processed_day2.png
│   └── raw.png
├── pyproject.toml
├── README.md
├── reports
│   └── missingness_orders.csv
├── scripts
│   ├── run_day1_load.py
│   └── run_day2_clean.py
├── src
│   └── data_workflow
│       ├── __init__.py
│       ├── config.py
│       ├── io.py
│       ├── quality.py
│       └── transforms.py
└── uv.lock
```

## Setup
-  Create a virtual environment (at the project root):

    ```
    uv init
    ```
    ```
    uv sync
    ```

- Activate it:

    (Linux/Mac) 
    ```
    source .venv/bin/activate
    ``` 
    
    (Windows)
    ```
    .venv\Scripts\Activate.ps1
    ``` 

- Install dependencies:

    ```
    uv add pandas pyarrow httpx
    ```

##  How to Run
### Day 1: Basic ETL Pipeline
From the project root, run:

```
python scripts/run_day1_load.py
```
### Day 2: Data Quality and Cleaning
From the project root, run:

```
python scripts/run_day2_clean.py
```

## Example Input/Output
**Input: orders.csv**

<img src="images/raw.png" width="400">


**output: orders.parquet**

<img src="images/processed_day1.png" width="400">


**output: orders_clean.parquet**

<img src="images/processed_day2.png" width="400">