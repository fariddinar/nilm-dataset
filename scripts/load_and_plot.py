import pandas as pd
import matplotlib.pyplot as plt
import os

csv_path = "../data/05-16 8h/S1P1.csv" # path to csv file 
df = pd.read_csv(csv_path)

print(df.head())

plt.plot(df['time'], df['p_active'], label='Active Power (W)')
plt.xlabel("Time (s)")
plt.ylabel("Power (W)")
plt.title(f"Power Consumption - {os.path.basename(csv_path)}")
plt.legend()
plt.show()
