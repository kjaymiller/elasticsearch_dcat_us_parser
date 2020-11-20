from elasticsearch import Elasticsearch 
import os

username, password = (
        os.environ.get('ELASTIC_USERNAME','elastic'),
        os.environ.get('ELASTICSEARCH_PASSWORD'),
        )

client = Elasticsearch(
        cloud_id=os.environ['CLOUD_ID'],
        # hosts = ['localhost'], for local instance
        http_auth=(username, password),
        )


