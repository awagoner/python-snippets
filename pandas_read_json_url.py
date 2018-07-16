# Import an URL
import pandas as pd

url = ('http://api.company.com/resource/voters.json?$limit=5')

pd.read_json(url, orient="records")
