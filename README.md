# ETL Pipeline
Implements **ETL (Extract, Transform, Load) pipeline** using Python and Pandas.

## Features
- Extracts raw data from CSV files
- Transforms and cleans the data by enforcing a schema
- Loads the processed data into Parquet files

## Project Structure
```
.
├── data
│   ├── cache
│   ├── external
│   ├── processed
│   │   ├── orders.parquet
│   │   └── users.parquet
│   └── raw
│       ├── orders.csv
│       └── users.csv
├── images
│   ├── processed.png
│   ├── project_structure.png
│   └── raw.png
├── main.py
├── pyproject.toml
├── README.md
├── reports
│   └── figures
├── scripts
│   └── run_day1_load.py
├── src
│   └── data_workflow
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-311.pyc
│       │   ├── config.cpython-311.pyc
│       │   ├── io.cpython-311.pyc
│       │   └── transforms.cpython-311.pyc
│       ├── config.py
│       ├── io.py
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

## How to Run the Pipeline
From the project root, run:

```
python scripts/run_day1_load.py
```

## Example Input/Output
**Input: orders.csv**

<img src="images/raw.png" width="400">

**Output: orders.parquet**

<img src="images/processed.png" width="400">