import os
import pandas as pd

folder_path = "../data/05-16 8h" # path to a specific data folder

appliance_map = {
    "S1P1.csv": "Hair dryer",
    "S1P2.csv": "Electric water heater",
    "S1P3.csv": "Aggregate",
    "S2P4.csv": "Hair straightener",
    "S2P5.csv": "Fridge",
    "S3P7.csv": "Iron",
    "S3P8.csv": "Screen",
    "S4P10.csv": "Laptop charger",
    "S4P11.csv": "Lamp"
}

summary = []

for i in range(1, 13):
    sensor_id = (i - 1) // 3 + 1
    filename = f"S{sensor_id}P{i}.csv"

    file_path = os.path.join(folder_path, filename)

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        appliance_name = appliance_map.get(filename, "Unknown")

        stats = {
            'File': filename,
            'Appliance': appliance_name,
            'Mean Power (W)': df['p_active'].mean(),
            'Max Power (W)': df['p_active'].max(),
            'Std Power (W)': df['p_active'].std()
        }
        summary.append(stats)
    else:
        print(f"Missing: {filename}")

summary_df = pd.DataFrame(summary)
print(summary_df)
