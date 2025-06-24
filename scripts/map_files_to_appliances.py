import os
import pandas as pd

folder_path = "../data/05-16 8h" # path to a specific data folder

appliance_map = {
    "S1P1.csv": "Hair dryer",
    "S1P2.csv": "Electric water heater",
    "S1P3.csv": "Aggregate 1",
    "S2P4.csv": "Hair straightener",
    "S2P5.csv": "Fridge",
    "S3P7.csv": "Iron",
    "S3P8.csv": "Screen",
    "S4P10.csv": "Laptop charger",
    "S4P11.csv": "Lamp"
}

mapping_info = []

for filename, appliance_name in appliance_map.items():
    file_path = os.path.join(folder_path, filename)
    if os.path.exists(file_path):
        mapping_info.append({
            "File": filename,
            "Appliance": appliance_name
        })
    else:
        print(f"Warning: {filename} not found in {folder_path}")

mapping_df = pd.DataFrame(mapping_info)
print(mapping_df)

# Save to CSV
# output_path = os.path.join(folder_path, "file_appliance_mapping.csv")
# mapping_df.to_csv(output_path, index=False)
