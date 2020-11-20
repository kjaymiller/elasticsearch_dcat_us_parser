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
    for dataset in datasets:
        dataset['_id'] = gen_id(dataset['identifier'], dataset['contactPoint']['fn'])
        dataset["city"] = kwargs.get('city', '')
        dataset["region"] = kwargs.get('region', '')
        url = dataset['identifier'].replace('_', '-')

        if url.endswith('gis'):
            url = url[:-4]
        dataset['url'] = kwargs.get('base_url') + "/" + url
        yield dataset


def upload(dataset: typing.Sequence, *, client, index, **kwargs):
        bulk(
            client=client,
            index=index,
            actions=modify_dataset(dataset, **kwargs),
        )
