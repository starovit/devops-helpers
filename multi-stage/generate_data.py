import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': np.random.rand(100),
    'B': np.random.randint(0, 100, 100),
    'C': np.random.choice(['X', 'Y', 'Z'], 100)
})

df.to_csv("random_data.csv", index=False)
