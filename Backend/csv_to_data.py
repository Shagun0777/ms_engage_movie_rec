import pandas as pd
import numpy as np
import math
def fetch_csv_to_data_dict(url):
    data = pd.read_csv(url)
    headers = data.keys().to_list()
    a= data.values.tolist()
    data_dict = []
    for row in a:
        dd = {}
        for i, j in zip(headers, row):
            try:
                if math.isnan(j):
                    j = ''
            except:
                pass
            dd[i]=j
        data_dict.append(dd)
    return data, data_dict