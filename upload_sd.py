import os
import json
from dcat_parser import upload, gen_id, modify_url
from connection import client

es_index = os.environ.get("ES_INDEX")
input_file = "data.json"

with open(input_file) as json_file:
    dataset = json.load(json_file)["dataset"],
    base_url="https://data.sandiego.gov/datasets/"
    stem = dataset['identifier'].replace('_', '-')

    if stem.endswith('gis'):
        stem = stem[:-4]
    url = modify_url(base_url, stem)
    _id=gen_id(dataset['identifier'], dataset['contactPoint']['fn']))
    upload(
            dataset=dataset,
            client=client,
            index = es_index,
            _id=_id,
            url=url,
            city="San Diego",
            region="California",
            base_url=base_url,
            portal = {
                "name": "San Diego Open Data Portal",
                "url": url,
                },
    )
