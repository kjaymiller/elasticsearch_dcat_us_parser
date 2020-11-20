"""Load JSON File and Load the Data into Elasticsearch"""

import hashlib
import json
import typing

from elasticsearch.helpers import bulk
from connection import client

es_index = os.environ.get("ES_INDEX")
input_file = "data.json"

def gen_id(*args):
    """Create an unique identifier based on the identifier and contactPoint
    of the dcat data
    """
    return hashlib.sha1(''.join(args).encode("utf-8")).hexdigest()


def modify_dataset(dataset):
    for dataset in datasets:
        dataset['_id'] = gen_id(dataset['contactPoint']['fn'], dataset['identifier'])
        dataset["city"] = city
        dataset["region"] = region
        yield dataset
        


def upload(dataset: typing.Sequence, *args, **kwargs):
    """Set the region to <State>, Country Abbreviation"""

    with open(input_file) as json_file:
        bulk(
            client=client,
            index=es_index,
            actions=modify_dataset(json.load(json_file)["dataset"], *kwargs, **kwargs),
        )
