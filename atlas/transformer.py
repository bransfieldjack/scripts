import numpy as np
import pandas as pd
import functools 
import csv
import pymongo
from pymongo import MongoClient


def main():


    MONGO_URI='mongodb://localhost:27017'


    """
    blood_atlas_samples_v7.1.tsv
    """
    blood_df = pd.read_csv('blood_atlas_samples_v7.1.tsv', sep='\t', index_col=0)
    blood_df.reset_index(level=0, inplace=True)
    row_list = blood_df['row_id'].values.tolist()

    blood_samples = []
    blood_dataset_ids = []
    

    for item in row_list:
        split = item.split(';')
        blood_samples.append(split[0])
        blood_dataset_ids.append(int(split[1]))

    distinct_blood_dataset_ids = list(set(blood_dataset_ids)) # Distinct values, the ds-ids were attached to all sample ids (duplicated).
    distinct_blood_samples = list(set(blood_samples)) # Distinct values, the ds-ids were attached to all sample ids (duplicated).


    """
    imac_atlas_samples_v7.1.tsv
    """
    imac_df = pd.read_csv('imac_atlas_samples_v7.1.tsv', sep='\t', index_col=0)
    imac_df.reset_index(level=0, inplace=True)
    row_list = imac_df['row_id'].values.tolist()

    imac_samples = []
    imac_dataset_ids = []

    for item in row_list:
        split = item.split(';')
        imac_samples.append(split[0])
        imac_dataset_ids.append(int(split[1]))

    distinct_imac_dataset_ids = list(set(imac_dataset_ids)) # Distinct values, the ds-ids were attached to all sample ids (duplicated).
    distinct_imac_samples = list(set(imac_samples)) # Distinct values, the ds-ids were attached to all sample ids (duplicated).


###################################################################################################################################################################################


    """
    Existing data in the portal (datasets, include blood): 
    """
    atlas_df = pd.read_csv('atlas_data_backup_31032020.tsv', sep='\t', index_col=0)
    atlas_df.reset_index(level=0, inplace=True)
    dataset_id_list = atlas_df['dataset_id'].unique().tolist() #.values.tolist().unique()

    dataset_id_include_blood = atlas_df.loc[atlas_df.include_blood=='t', ['dataset_id', 'include_blood']].values.tolist()

    flattened = []

    for item in dataset_id_include_blood:
        for subitem in item:
            flattened.append(subitem)

    result = list(filter(('t').__ne__, flattened))

    unique = []

    for x in result:
        if x not in unique:
            unique.append(x)

    # print(len(unique))


    # """
    # Existing data in the portal (datasets, include imac): 
    # """
    # atlas_df = pd.read_csv('atlas_data_backup_31032020.tsv', sep='\t', index_col=0)
    # atlas_df.reset_index(level=0, inplace=True)
    # dataset_id_list = atlas_df['dataset_id'].unique().tolist() #.values.tolist().unique()

    # dataset_id_include_blood = atlas_df.loc[atlas_df.include_imac=='t', ['dataset_id', 'include_imac']].values.tolist()

    # flattened = []

    # for item in dataset_id_include_blood:
    #     for subitem in item:
    #         flattened.append(subitem)

    # result = list(filter(('t').__ne__, flattened))

    # unique = []

    # for x in result:
    #     if x not in unique:
    #         unique.append(x)

    # print("jarnys;")
    # print(len(distinct_imac_dataset_ids))

    # print("mine:")
    # print(len(unique))


    # """
    # Existing data in the portal (samples, include imac): 
    # """
    # atlas_df = pd.read_csv('atlas_data_backup_31032020.tsv', sep='\t', index_col=0)
    # atlas_df.reset_index(level=0, inplace=True)
    # sample_id_list = atlas_df['sample_id'].unique().tolist() #.values.tolist().unique()

    # sample_id_include_blood = atlas_df.loc[atlas_df.include_blood=='t', ['sample_id', 'include_blood']].values.tolist()

    # flattened = []

    # for item in sample_id_include_blood:
    #     for subitem in item:
    #         flattened.append(subitem)

    # result = list(filter(('t').__ne__, flattened))

    # unique = []

    # for x in result:
    #     if x not in unique:
    #         unique.append(x)

    # print("jarnys;")
    # print(len(distinct_blood_samples))

    # print("mine:")
    # print(len(unique))


###################################################################################################################################################################################


    """
    Correct data on the atlas page:
    """

    # print(distinct_blood_dataset_ids)
    # print(distinct_blood_samples)

    # print(distinct_imac_dataset_ids)
    # print(distinct_imac_samples)


###################################################################################################################################################################################


    """
    Existing data in the portal (datasets, include imac): 
    """
    atlas_df = pd.read_csv('atlas_data_backup_31032020.tsv', sep='\t', index_col=0)
    # atlas_df.reset_index(level=0, inplace=True)

    blood_dataframes_list = []
    imac_dataframes_list = []

    for item in distinct_blood_dataset_ids:

        result = atlas_df.loc[item, :]
        new_df = pd.DataFrame(result).drop_duplicates()
        # new_df.reset_index(level=0, inplace=True)
        df_to_dict = new_df.to_dict('records')
        _dict = {
            "dataset_id": item,
            "data": df_to_dict,
        }
        blood_dataframes_list.append(_dict)

    
    for item in blood_dataframes_list:

        myclient = pymongo.MongoClient(MONGO_URI) # Mongon container name is 'mongo'. # local mongodb server.   # Connects to the mongodb daabase and returns everything.
        database = myclient["atlas"]
        collection = database["blood"]
        result = collection.insert(item)

    for item in distinct_imac_dataset_ids:

        result = atlas_df.loc[item, :]
        new_df = pd.DataFrame(result).drop_duplicates()
        # new_df.reset_index(level=0, inplace=True)
        df_to_dict = new_df.to_dict('records')
        _dict = {
            "dataset_id": item,
            "data": df_to_dict,
        }
        imac_dataframes_list.append(_dict)

    
    for item in imac_dataframes_list:

        myclient = pymongo.MongoClient(MONGO_URI) # Mongon container name is 'mongo'. # local mongodb server.   # Connects to the mongodb daabase and returns everything.
        database = myclient["atlas"]
        collection = database["imac"]
        result = collection.insert(item)

    print("Operation complete")



if __name__ == "__main__":
    main()



