import csv
import glob
import os
from elasticsearch import helpers, Elasticsearch

es = Elasticsearch()

for path in glob.glob("*.csv"):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='|')
        csv_name = os.path.splitext(path)[0]
        helpers.bulk(es, reader, index="index1", doc_type=csv_name)
