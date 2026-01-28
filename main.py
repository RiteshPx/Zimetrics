#import libraries
import pandas as pd

USD_TO_INR = 83 # Conversion rate from USD to INR (Given in the question)

def main(input_file="sales.csv", output_file="clean_sales.json"):
    """Clean messy sales CSV and output JSON report."""

    print("Reading sales.csv...")

    df = pd.read_csv(input_file, header=None,
                    names=["id", "product", "price", "country"],
                    encoding="utf-8",
                    skipinitialspace=True)

    print(f'Total number of rows in original data: {len(df)}')


    # Remove irrelevant " in product column
    df["product"] = df["product"].str.replace('"', '', regex=False).str.strip()

    #remove $ in price column
    df["price"] = (df["price"].str.replace("$", "", regex=False)
                   .str.strip().astype(float))

    # Remove rows with missing values
    print('Number of null values per column:')
    print(df.isnull().sum())
    df = df.dropna()
    print(f'Total number of rows after removing null values: {len(df)}')

    #check for duplicates and remove them
    print(f'Total number of duplicate rows: {df.duplicated(subset=["product", "price"]).sum()}')
    df = df.drop_duplicates(subset=["product", "price"])
    print(f'Total number of rows after removing duplicates: {len(df)}')

    # Convert price from USD to INR 
    df["price_inr"] = (df["price"] * USD_TO_INR).round(2)


    # Rename for clarity
    df = df.rename(columns={"price": "price_usd"})
    # Reorder columns
    df = df[["id", "product", "price_usd", "price_inr", "country"]]


    # Save cleaned data to a new JSON file
    df.to_json(output_file, orient="records", indent=4)
    print(f"{output_file} created successfully!")


if __name__ == "__main__":
    main("raw_data/sales.csv", "clean_sales.json")