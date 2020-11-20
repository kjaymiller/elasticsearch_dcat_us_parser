import os
import json
from dcat_parser import upload
from connection import client

es_index = os.environ.get("ES_INDEX")
input_file = "data.json"

with open(input_file) as json_file:
    upload(
            json.load(json_file)["dataset"],
            client=client,
            index = es_index,
            city="San Diego",
            region="California",
            base_url="https://data.sandiego.gov/datasets/"
            )
