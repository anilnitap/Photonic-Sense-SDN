# Photonic-Sense-SDN

This repository contains the synthetic dataset and simulation script used in the research paper:

**On-chip Plasmonic framework for scalable real1 time sensor networks2**  
_(Submitted to JOSA B, 2025)_

---

## 📁 Repository Structure

Photonic-Sense-SDN/
├── dataset/
│ └── Photonic_Sense_SDN.csv # Generated sensor event dataset
├── scripts/
│ └── simulate_sensor_traffic.py 
├── README.md # Project overview and usage
├── LICENSE # MIT License
└── .gitignore # Common exclusions

## 📊 Dataset Description

**`Photonic_Sense_SDN.csv`** simulates on-chip photonic sensor events monitored and managed by an SDN controller.

| Column                    | Description                                  |
|---------------------------|----------------------------------------------|
| `Event_ID`                | Unique identifier for each sensor event      |
| `Timestamp`               | Date and time of event generation            |
| `Event_Class`             | Type of event: `Normal` or `Emergency`       |
| `Latency_ms`              | End-to-end latency of data packet (in ms)    |
| `Reconfiguration_Time_ms`| Time taken for flow reconfiguration (in ms)  |
| `Packet_Delivery_Ratio`  | % of packets delivered successfully          |
| `Controller_CPU_Load`    | SDN controller CPU load during the event (%) |

## 🔧 Requirements

- Python 3.8+
- pandas
- matplotlib (optional for visualizations)

Install dependencies (if needed):

```bash
pip install pandas matplotlib
