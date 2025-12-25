# ETL Pipeline with EDA & Visualization
Structured ETL pipeline with data quality validation, analytics table construction, and exploratory data analysis using Python, Pandas, and Plotly.

## Features
- Extracts and validates CSV data
- Enforces schema and type validation
- Creates missingness reports and adds missing value flags
- Normalizes text data
- Parses datetime columns and extracts time components
- Performs safe left joins with validation
- Detects and handles outliers
- Builds analytics tables for analysis
- Generates interactive visualizations with Plotly
- Exports to Parquet with logging
- Production-ready ETL orchestration
- Run metadata generation for reproducibility

## Project Structure
```
.
├── data
│   ├── cache
│   ├── external
│   ├── processed
│   │   ├── _run_meta.json
│   │   ├── analytics_table.parquet
│   │   ├── orders_clean.parquet
│   │   ├── orders.parquet
│   │   └── users.parquet
│   └── raw
│       ├── orders.csv
│       └── users.csv
├── notebooks
│   └── eda.ipynb
├── pyproject.toml
├── README.md
├── reports
│   ├── figures
│   │   ├── amount_distribution.png
│   │   ├── revenue_by_country.png
│   │   ├── revenue_trend_monthly.png
│   │   ├── status_distribution.png
│   │   └── top10_countries.png
│   ├── missingness_orders.csv
│   └── summary.md
├── scripts
│   ├── run_day1_load.py
│   ├── run_day2_clean.py
│   ├── run_day3_build_analytics.py
│   └── run_etl.py
├── src
│   └── data_workflow
│       ├── __init__.py
│       ├── config.py
│       ├── etl.py
│       ├── io.py
│       ├── joins.py
│       ├── quality.py
│       ├── transforms.py
│       ├── utils.py
│       └── viz.py
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
    uv add pandas pyarrow httpx plotly kaleido nbformat
    ```

## How to Run

**Important: Scripts must be run in sequential order**

### Day 1: Basic ETL Pipeline

From the project root, run:
```bash
python scripts/run_day1_load.py
```

### Day 2: Data Quality and Cleaning

From the project root, run:
```bash
python scripts/run_day2_clean.py
```

### Day 3: Analytics Table Construction

From the project root, run:
```bash
python scripts/run_day3_build_analytics.py
```

### Day 4: Exploratory Data Analysis

Open and run the Jupyter notebook:
```bash
jupyter notebook notebooks/eda.ipynb
```

Or use VS Code to open `notebooks/eda.ipynb` and run all cells.

### Day 5: Production ETL Pipeline

From the project root, run:
```bash
python scripts/run_etl.py
```
