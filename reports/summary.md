# Summary of Findings and Caveats

## Key Findings

- **Total Revenue**: SA accounts for $145.50 in total revenue, while AE accounts for $0.00
- **Order Volume**: SA has 4 orders (80%), AE has 1 order (20%)
- **Order Status**: 4 orders are paid (80%), 1 order is refund (20%)
- **Average Order Value**: Mean is $35.85, median is $18.75

## Definitions

- **Revenue**: Sum of `amount` column over all orders with status 'paid'
- **AOV (Average Order Value)**: Mean of `amount` column for paid orders
- **Refund rate**: Proportion of orders where `status_clean == "refund"`
- **Time window**: December 2025
- **Winsorized amount**: Order amounts capped at 1st and 99th percentiles to reduce outlier impact on visualizations

## Data Quality Caveats

### Missingness
- 20% of orders have missing `created_at` values (1 out of 5 orders)
- 20% of orders have missing `amount` values (1 out of 5 orders)

### Duplicates
- No duplicate order IDs found in the dataset

### Join Coverage
- 100% of orders successfully matched to users table

### Outliers
- 1 order flagged as outlier with amount > $97.75
- Charts use winsorized values for readability

### Other Issues
- Small dataset (5 orders total) limits statistical significance
- Limited time range (December 2025 only)

## Next Questions

- How does revenue trend over longer time periods?
- What is the customer lifetime value by country?
- Are there patterns in refund behavior?
- What factors predict high-value orders?

## Technical Notes

- **ETL Pipeline**: Run `python scripts/run_etl.py` to reproduce processed outputs
- **Run Metadata**: See `data/processed/_run_meta.json` for run details
- **Data Source**: Raw data in `data/raw/`, processed outputs in `data/processed/`
- **EDA Notebook**: See `notebooks/eda.ipynb` for detailed analysis