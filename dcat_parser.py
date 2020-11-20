"""Load JSON File and Load the Data into Elasticsearch"""

import json
from connection import client
from elasticsearch.helpers import bulk
import hashlib
import typing
import pathlib
import os
from markdown2 import markdown
import itertools

es_index = os.environ.get('ES_INDEX')
input_file = 'data.json'

## TODO: Add Descriptions to Posts

def set_descriptions(dataset, working_dir):
    basename = dataset['identifier']
    working_directory = pathlib.Path(working_dir)

    if (identifier:=working_directory.join(basename).with_suffix('.md')).exists():
        return identifies.read_text()
    
    elif (identifier:=working_directory.join(basename[:4]).with_suffix('.md')).exists():
        return identifies.read_text()

    else:
        return ''


def strip_table_from_markdown(markdown_text):
    lines = reversed(markdown_text.splitlines(keepends=True))
    main_text = list(itertools.takewhile(lambda x: not x.strip().startswith('--'), lines))
    print(''.join(main_text[::-1]))


def set_city_region(dataset:str, *, city:str, region:str):
    """Append the city and region to your data"""
    dataset['city'] = city
    dataset['region'] = region


def gen_id(datasets: typing.List, *, city:str, region:str):
    """Create an unique identifier based on the identifier and contactPoint
    of the dcat data
    """
    _id = dataset['contactPoint']['fn'] + dataset['identifier']
    dataset['_id'] = hashlib.sha1(_id.encode('utf-8')).hexdigest()

def modify_data(dataset, **kwargs):
    for dataset in datasets:

        gen_id() 
        yield new_data


def parse(city:str , region:str):
    """Set the region to <State>, Country Abbreviation"""

    with open(input_file) as json_file:
        bulk(
            client=client,
            index=es_index,
            actions=modify_data(json.load(json_file)['dataset'], city, region),
            )


if __name__ == '__main__':
    parse()
