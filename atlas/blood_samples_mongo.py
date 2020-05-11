import numpy as np
import pandas as pd
import functools 
import csv
import pymongo
from pymongo import MongoClient


"""
Converts the existing atlas blood samples to a mongo collection.
"""

def main():

    MONGO_URI='mongodb://localhost:27017'

    """
    blood_atlas_samples_v7.1.tsv
    Construct a dataframe from the text file dump and convert into a new format with new column/fields. 
    """

    blood_df = pd.read_csv('./data/blood/blood_atlas_samples_v7.1.tsv', sep='\t', index_col=0)
    blood_df.reset_index(level=0, inplace=True)
    row_list = blood_df['row_id'].values.tolist()
    blood_df.set_index('row_id', inplace=True)
    blood_df.columns = ['progenitor_type', 'sample_source', 'cell_type']

    convert_list = blood_df.index.tolist()
    dataset_ids = []
    sample_ids = []

    for item in blood_df.index.tolist():
        split = item.split(';')
        sample_ids.append(split[0])
        dataset_ids.append(split[1])

    blood_df['dataset_id'] = dataset_ids
    blood_df['sample_id'] = sample_ids
    blood_df.reset_index(drop=True, inplace=True)
    blood_df['annotator'] = ""
    blood_df['evidence'] = ""
    blood_df['phenotype'] = ""
    blood_df['activation_status'] = ""
    blood_df['display_metadata'] = ""
    blood_df['include_blood'] = ""
    new_df = blood_df[['sample_id', 'annotator', 'evidence', 'progenitor_type', 'sample_source', 'cell_type', 'phenotype', 'activation_status', 'display_metadata', 'include_blood', 'dataset_id']]
    new_df.set_index('dataset_id', inplace=True)

    """
    For every unique dataset_id in the new dataframe, construct a dataframe for that ID and write it to the mongo blood database. 
    """

    unique_blood_dataset_id_list = list(set(dataset_ids))

    mongo_list = []
    
    for item in unique_blood_dataset_id_list:
        result = new_df.loc[item, :]
        final_df = pd.DataFrame(result) #.drop_duplicates()

        df_to_dict = final_df.to_dict('records')
        _dict = {
            "dataset_id": item,
            "data": df_to_dict,
        }
        mongo_list.append(_dict)
        
    for item in mongo_list:

        myclient = pymongo.MongoClient(MONGO_URI) # Mongon container name is 'mongo'. # local mongodb server.   # Connects to the mongodb daabase and returns everything.
        database = myclient["blood_v1"]
        collection = database["samples"]
        result = collection.insert(item)

    print("Operation complete")


if __name__ == "__main__":
    main()
