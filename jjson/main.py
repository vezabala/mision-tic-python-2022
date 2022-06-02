import json
import pandas as pd
import requests

resp = requests.get('Files/json/bands_errado.json')
print(json.loads(resp.content))

