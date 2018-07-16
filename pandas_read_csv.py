import pandas as pd

# Import a file
pd.read_json("/files/data/sample.json", orient="records", lines=True,)
