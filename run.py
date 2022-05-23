from fileinput import filename
import os,time
from datetime import datetime
import shutil

def main():
    while(True):
        backup_frequency = os.environ['BACKUP_FREQUENCY', 60]
        backup_data()
        delete_old_files()  
        time.sleep(backup_frequency*60)

def backup_data():

    fileName = datetime.now().strftime("%Y_%m_%d-%H_%M_%S_%p")
    source = "/saves"
    destination= "/backups"

    shutil.make_archive(base_name=(os.path.join(destination,fileName)), format="zip", root_dir=source)

def delete_old_files():
    backup_age = os.environ['BACKUP_AGE',1]
    destination= "/home/kaz/DockerFiles/backups"
           
    # files_list = os.listdir(destination)
    # current_time = time.time()
    # for backup_files in files_list:
    #     file_path = os.path.join(destination, backup_files)
    #     if os.path.isfile(file_path):
    #         if (current_time - os.stat(file_path).st_birthtime) > backup_age * 86400:
    #             os.remove(file_path)

if __name__=="__main__":
    main()

