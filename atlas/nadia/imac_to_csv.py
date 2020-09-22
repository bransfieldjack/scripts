import numpy as np
import pandas as pd
import functools 
import csv
import pymongo
from pymongo import MongoClient
from functools import reduce


"""
Exporting the imac_v1/samples collection to a .csv file for Nadia. 
Including the 'tissue type' and 'disease' columns, as requested by her.
"""

def main():

    samples_non_merged = pd.read_csv('imac_v1_samples_non_merged.csv')


    samples_in_myeloid = pd.read_csv('samples_in_myeloid.csv')
    
    res = pd.merge(samples_non_merged, samples_in_myeloid).drop_duplicates()
    res.to_csv('samples_myeloid_merged.csv')
    
    # print(res)
    # print(samples_non_merged.reset_index(drop=True))
    # result = pd.concat([samples_non_merged, samples_in_myeloid]).drop_duplicates()

    # result.to_csv('samples_myeloid_merged.csv')

    # print(result)

    # semi_final_result.to_csv('samples_myeloid_merged.csv', index=False)

    # frames = [samples_non_merged, samples_in_myeloid]
    # result = pd.concat(frames, join='outer', ignore_index=False, keys=None)

    # print(result)
    # result.to_csv('samples_myeloid_merged.csv')
    # print(result)

    # MONGO_URI='mongodb://localhost:27017'
    # myclient = pymongo.MongoClient(MONGO_URI)

    # imac_database = myclient["imac_v1"]
    # imac_collection = imac_database["samples"]
    # imac_result = imac_collection.find()

    # df_list = []
    # ds_ids = []
    # for item in imac_result:
    #     del item['_id']

    #     for sub_item in item['data']:
    #         sub_item['dataset_id'] = item['dataset_id']
    #         ds_ids.append(item['dataset_id'])
    #         df_list.append(sub_item)

    # myset_ids = set(ds_ids)
    # unique_ds_ids = list(myset_ids)

    # samples_latest = pd.read_csv('samples_latest.csv')
    # # samples_latest.reset_index(level=0, inplace=True)
    # # print(samples_latest)
       
    # l1=[]
    # for ds_id in unique_ds_ids:
    #     newdf = samples_latest.loc[samples_latest['dataset_id'] == int(ds_id)]
    #     l1.append(newdf)
    
    # pd.concat(l1).to_csv('samples_in_myeloid.csv')

    # samples_latest = pd.read_csv('samples_latest.csv', index_col=0)
    # samples_latest.reset_index(level=0, inplace=True)

    # # print(samples_latest)

    # samples_latest_list = []
    # for _id in unique_ds_ids:
    #     res = samples_latest.loc[samples_latest['dataset_id'] == int(_id)]
    #     final = res.to_dict('records')
    #     samples_latest_list.append(final)

    # flat_list = []
    # for sublist in samples_latest_list:
    #     for item in sublist:
    #         flat_list.append(item)

    # final_flat_list = pd.DataFrame(df_list)
    # # print(final_df_list)

    # final_df_list = pd.DataFrame(flat_list)
    # # print(final_df_list)

    # dfList = [final_flat_list, final_df_list]

    # final_df = reduce(lambda x, y: pd.merge(x, y, on = 'dataset_id'), dfList)

    # print(final_df)

    # for item in df_list:
    #     print(item)
    # print(df_list)
    # print(flat_list)

    # joinedlist = df_list + flat_list

    # keys = list(joinedlist[0].keys()) + list(joinedlist[-1].keys())
    # set_dict = set(keys)
    # keys_list = list(set_dict)    

    # with open('imac_v1_samples_columns_to_join.csv', 'w', newline='')  as output_file:
    #     dict_writer = csv.DictWriter(output_file, keys_list)    # dict writer maintains order.
    #     dict_writer.writeheader()
    #     dict_writer.writerows(final_test)


    ###########################
    # Testing
    ###########################

    # test_list = []
    # for item in joinedlist:
    #     test_list.append(item['dataset_id'])

    # print(len(set(test_list)))


if __name__ == "__main__":
    main()


