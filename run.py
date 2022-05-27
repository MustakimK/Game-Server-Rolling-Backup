import os,time
from datetime import datetime
import shutil

def main():
    BACKUP_FREQUENCY_CONSTANT = '60'
    BACKUP_AGE_CONSTANT = '1'
    SOURCE_DIR_CONSTANT = '/saves'
    DESTINATION_DIR_CONSTANT = '/backups'

    backup_frequency = os.getenv('BACKUP_FREQUENCY', BACKUP_FREQUENCY_CONSTANT)
    backup_age = os.getenv('OLDEST_BACKUP_AGE', BACKUP_AGE_CONSTANT)
    source_dir = os.getenv('SAVE_DIR', SOURCE_DIR_CONSTANT)
    destination_dir = os.getenv('BACKUP_DIR', DESTINATION_DIR_CONSTANT)

    backup_frequency = convert_to_seconds(backup_frequency)
    backup_age = convert_to_seconds(backup_age)

    print(backup_age,backup_frequency)

    while(True):
        
        fileName = datetime.now().strftime("%Y_%m_%d-%H_%M_%S_%p")

        backup_data(destination_dir, fileName, source_dir)
        delete_old_files(backup_age, destination_dir)
        time.sleep(backup_frequency)

def backup_data(destination_dir, fileName, source_dir):
    shutil.make_archive(base_name=(os.path.join(destination_dir,fileName)), format="zip", root_dir=source_dir)

def delete_old_files(backup_age, destination_dir):

    list_of_files = os.listdir(destination_dir)

    for filename in list_of_files:

        path = os.path.join(destination_dir, filename)
        modified_time = os.path.getmtime(path)

        if time.time()-modified_time > (backup_age): #* 86400): #time in seconds
            os.remove(path)

def convert_to_seconds(time_string):
    units_in_seconds = {'m': 2628000, 'w': 604800, 'd': 86400, 'h': 3600, 'm': 60, 's': 1}

    return (int(time_string[:-1]) * (units_in_seconds[time_string[-1].lower()]))

if __name__=="__main__":
    main()