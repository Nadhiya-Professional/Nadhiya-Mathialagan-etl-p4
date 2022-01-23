import google.cloud.storage as gcs
import logging
import os

if __name__ == '__main__':
    bucket_name = "york-project-bucket"
    destination_file_name = "Output.csv"
    storage_client = gcs.Client()
    bucket = storage_client.bucket(bucket_name)
    file_open = open("final_output.csv",'a')
    string_append = "author,score"
    file_open.write(string_append)
    file_open.write('\n')
    for i in range(0,37):
        if i < 10:
            source_blob_name = eval(f'"nadhiya/2021-12-17-18-15/part-r-0000{i}"')
            blob = bucket.blob(source_blob_name)
            blob.download_to_filename(destination_file_name)
            f1=open(destination_file_name,'r')
            file_open.write(f1.read())
            print(source_blob_name)

        else:
            source_blob_name = eval(f'"nadhiya/2021-12-17-18-15/part-r-000{i}"')
            blob = bucket.blob(source_blob_name)
            blob.download_to_filename(destination_file_name)
            file_open.write(destination_file_name)
            f1 = open(destination_file_name, 'r')
            file_open.write(f1.read())
            print(source_blob_name)
    print("done")