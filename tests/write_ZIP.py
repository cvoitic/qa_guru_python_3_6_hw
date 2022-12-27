import zipfile
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
tmp_dir = os.path.join(current_dir, '../resources')
file_dir = os.listdir(tmp_dir)

with zipfile.ZipFile('../resources/myzip.zip', 'w') as archive:
    for file in file_dir:
        add_file = os.path.join(tmp_dir, file)
        archive.write(add_file)

with zipfile.ZipFile('../resources/myzip.zip', 'a') as archive:
    for file in archive.namelist():
        print(file)

archive.close()






