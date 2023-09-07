import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os
pwd = os.getcwd()

# Sample data
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

def random_time(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

# Generate dataset
data = {
    'Train_ID': [i for i in range(100)],
    'Origin': [random.choice(cities) for _ in range(100)],
    'Destination': [random.choice(cities) for _ in range(100)],
    'Departure_Time': [random_time(datetime(2023, 9, 10, 8), datetime(2023, 9, 10, 20)) for _ in range(100)],
    'Arrival_Time': [random_time(datetime(2023, 9, 10, 20), datetime(2023, 9, 11, 8)) for _ in range(100)],
    'Ticket_Price': [round(np.random.normal(50, 15), 2) for _ in range(100)],
    'Seats_Available': [random.randint(10, 60) for _ in range(100)]
}

# Create dataframe
df = pd.DataFrame(data)

# To prevent Origin and Destination being the same
df = df[df['Origin'] != df['Destination']].reset_index(drop=True)

# Display
print(df.head(10))
# ... (rest of the code)

# Save the dataframe to CSV
df.to_csv(pwd +'\synthetic_railway_dataset.csv', index=False)
