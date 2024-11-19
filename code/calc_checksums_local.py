import os
import hashlib
import csv

root_dir = '/Users/tedwards/Documents/projects/P435_Tcell_differentiation_Khor/data_saved/counts_GEO'
csv_file_path = os.path.join(root_dir, 'checksums_py_local.csv')

with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['filename', 'md5_checksum']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for dir_name, sub_dir_list, file_list in os.walk(root_dir):
        for file_name in file_list:
            file_path = os.path.join(dir_name, file_name)
            md5_hash = hashlib.md5()
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    md5_hash.update(chunk)
                md5_checksum = md5_hash.hexdigest()
                writer.writerow({'filename': os.path.basename(file_path), 'md5_checksum': md5_checksum})