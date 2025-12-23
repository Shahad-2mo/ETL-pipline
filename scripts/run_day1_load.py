import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from data_workflow.config import make_paths
from data_workflow.io import read_orders_csv, read_users_csv, write_parquet
from data_workflow.transforms import enforce_schema


def main():

    paths = make_paths(ROOT)
    
    orders_path = paths.raw / "orders.csv"
    users_path = paths.raw / "users.csv"
    
    orders_raw = read_orders_csv(orders_path)
    users_raw = read_users_csv(users_path)
    
    orders_clean = enforce_schema(orders_raw)
    
    print("--- Data Quality Summary ---")
    missing_amount = orders_clean["amount"].isna().sum()
    missing_quantity = orders_clean["quantity"].isna().sum()
    print(f"Missing amounts: {missing_amount}")
    print(f"Missing quantities: {missing_quantity}")
    
    orders_output = paths.processed / "orders.parquet"
    users_output = paths.processed / "users.parquet"
    
    write_parquet(orders_clean, orders_output)
    write_parquet(users_raw, users_output)
    
    print("--- ETL Pipeline Complete --- ")
    print(f"  - orders.parquet ({len(orders_clean)} rows)")
    print(f"  - users.parquet ({len(users_raw)} rows)")

if __name__ == "__main__":
    main()