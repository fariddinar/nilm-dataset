# Capturing High-Frequency Harmonic Signatures for NILM: Building a Dataset for Load Disaggregation

This repository accompanies the paper:

**"Capturing High-Frequency Harmonic Signatures for NILM: Building a Dataset for Load Disaggregation"**

Dinar, F.; Paris, S.; Busvelle, É. Capturing High-Frequency Harmonic Signatures for NILM: Building a Dataset for Load Disaggregation. 2025

---

## Description

Our dataset provides electrical consumption data collected using synchronized sensor nodes, it also includes high-frequency electircal signatures such as current harmonics. The dataset is designed to support research in **Non-Intrusive Load Monitoring (NILM)**, focusing on appliance-level transient detection and load disaggregation. The dataset is collected using **ATM90E36A and ESP32 based custom sensor nodes**, each capable of recording synchronized various electrical signatures across multiple electrical phases.

## Key Features

* **Sensors**: 4 nodes with 3 phases each (12 total channels)
* **Data Format**: CSV files with columns : `time`, `irms`, `vrms`, `power_factor`, `p_apparente`, `p_active`, `h1-h32`
* **Appliances**: Hair dryer, Electric water heater, Fridge, Iron, Laptop charger, etc.

---

## Data structure

The data folder is structured as the following :
```
.
├── data                   
      └── 05-12 8h 
      │       └──S1P1.csv
      │       │    .
      │       │    .
      │       │    .
      │       └──S4P11.csv
      │		  .
      │		  .
      │		  .
      └── 06-18 6h 
      │       └──S1P1.csv
      │       │    .
      │       │    .
      │       │    .
      │       └──S4P11.csv
      │		  .
      │		  .
      │		  .   

```

---

## Dataset Contents

All datasets are stored in the `/data/` directory. Each folder (e.g., `05-16 8h/`) contains 12 CSV files named `SxPy.csv`, representing **Sensor x, Phase y**.

| File Name           | Appliance             | Description                    |
| ------------------- | --------------------- | ------------------------------ |
| `S1P1.csv`          | Hair Dryer            | Sensor 1, Phase 1              |
| `S1P2.csv`          | Electric Water Heater | Sensor 1, Phase 2              |
| `S1P3.csv`          | Aggregate             | Sensor 1, Phase 3              |
| `S2P4.csv`          | Hair Straightener     | Sensor 2, Phase 4              |
| `S2P5.csv`          | Fridge                | Sensor 2, Phase 5              |
| `S3P7.csv`          | Iron                  | Sensor 3, Phase 7              |
| `S3P8.csv`          | Screen                | Sensor 3, Phase 8              |
| `S4P10.csv`         | Laptop Charger        | Sensor 4, Phase 10             |
| `S4P11.csv`         | Lamp                  | Sensor 4, Phase 11             |

---

## Usage Example

Clone the repository and run the appliance mapping, loading and plotting script:

### Clone the repository
```
git clone https://github.com/fariddinar/nilm-dataset.git
```
### Change into the scripts directory
```
cd nilm-dataset/scripts
```

#### Run the appliance mapping script
```
python map_files_to_appliances.py
```

### To load and visualize a specific appliance signal:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/05-16 8h/S1P1.csv")
plt.plot(df["time"], df["p_active"])
plt.xlabel("Time (s)")
plt.ylabel("Active Power (W)")
plt.title("Hair Dryer")
plt.show()
```

---

## Citation

If you use this dataset in your work, please cite:

```
@article{farid2025,
  title={Capturing High-Frequency Harmonic Signatures for NILM: Building a Dataset for Load Disaggregation},
  author={Dinar Farid, Paris Sébastien, Busvelle Eric},
  journal={Sensors},
  year={2025},
  doi={}
}
```

---

## Contact

For questions, feedback, or collaboration opportunities:
📧 \[[dinar@univ-tln.fr](mailto:dinar@univ-tln.fr)]
