"""Load JSON File and Load the Data into Elasticsearch"""

import hashlib
import json
import typing

from elasticsearch.helpers import bulk

def gen_id(*args):
    """Create an unique identifier based on the identifier and contactPoint
    of the dcat data
    """
    return hashlib.sha1(''.join(args).encode("utf-8")).hexdigest()


def modify_dataset(datasets, **kwargs):
    """Compile key valies for dataset options"""
    for dataset in datasets:
        for x,y in kwargs.items():
            dataset[x] = y

        yield dataset


def upload(dataset: typing.Sequence, *, client, index, **kwargs):
        bulk(
            client=client,
            index=index,
            actions=modify_dataset(dataset, **kwargs),
        )
