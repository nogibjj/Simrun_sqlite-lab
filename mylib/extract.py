"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

Patient Satisfaction dataset
"""
import requests


def extract(
    url="https://raw.githubusercontent.com/nogibjj/Simrun_sqlite-lab/main/data/NC_data.csv",
    file_path="data/NC_data.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
