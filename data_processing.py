import csv
import glob
import os

data_folder = "data"
output_file = "combined_sales_data.csv"

file_pattern = os.path.join(data_folder, "daily_sales_data_*.csv")
file_list = glob.glob(file_pattern)

if not file_list:
    print(f"File not found: {file_pattern}")
    exit()

with open(output_file, "w", newline="", encoding="utf-8") as out_f:
    writer = csv.writer(out_f)
    writer.writerow(["Sales", "Date", "Region"])

    for file_path in sorted(file_list):
        print(f"Processing: {file_path}")

        with open(file_path, "r", newline="", encoding="utf-8") as in_f:
            reader = csv.DictReader(in_f) 

            for row in reader:
                if row["product"] != "pink morsel":
                    continue
                
                price_str = row["price"]
                price_str_clean = price_str.replace("$", "").replace(",", "").strip()

                try:
                    price = float(price_str_clean)
                except ValueError:
                    print(f"Warning: unable to parse price '{price_str}' skip this row")
                    continue

                qty_str = row["quantity"]
                qty_str_clean = qty_str.replace(",", "").strip()
                try:
                    quantity = int(qty_str_clean)
                except ValueError:
                    print(f"Warning: unable to parse quantity '{qty_str}' skip this row")
                    continue

                sales = price * quantity

                date_val = row["date"]
                region_val = row["region"]

                writer.writerow([sales, date_val, region_val])

print(f"Finish data processing! Save to: {output_file}")