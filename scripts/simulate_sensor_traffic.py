import pandas as pd
import random
from datetime import datetime

random.seed(42)

def generate_event(event_id):
    event_class = random.choice(['Normal'] * 8 + ['Emergency'] * 2)
    latency = random.uniform(10, 15) if event_class == 'Normal' else random.uniform(5, 10)
    reconfig_time = 0 if event_class == 'Normal' else random.uniform(4, 6)
    pdr = random.uniform(94, 98) if event_class == 'Normal' else random.uniform(98, 100)
    cpu_load = random.uniform(12, 18) if event_class == 'Normal' else random.uniform(22, 28)

    return {
        'Event_ID': event_id,
        'Timestamp': datetime.now().isoformat(),
        'Event_Class': event_class,
        'Latency_ms': round(latency, 2),
        'Reconfiguration_Time_ms': round(reconfig_time, 2),
        'Packet_Delivery_Ratio': round(pdr, 2),
        'Controller_CPU_Load': round(cpu_load, 2)
    }

def generate_dataset(num_events=200):
    events = [generate_event(i + 1) for i in range(num_events)]
    df = pd.DataFrame(events)
    df.to_csv('../dataset/Photonic_Sense_SDN.csv', index=False)
    print("Dataset saved to dataset/Photonic_Sense_SDN.csv")

if __name__ == "__main__":
    generate_dataset()
