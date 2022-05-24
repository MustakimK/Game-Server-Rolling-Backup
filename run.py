from email.policy import default
from fileinput import filename
import os,time
from datetime import datetime
import shutil

def main():
    backup_frequency = os.getenv('BACKUP_FREQUENCY', '60')
    backup_age = os.getenv('BACKUP_AGE', '1')
    
    source = "/saves"
    destination= "/backups"

    while(True):
        
        fileName = datetime.now().strftime("%Y_%m_%d-%H_%M_%S_%p")

        backup_data(destination, fileName, source)
        delete_old_files(backup_age, destination)  
        time.sleep(int(backup_frequency)*60)

def backup_data(destination, fileName, source):

    shutil.make_archive(base_name=(os.path.join(destination,fileName)), format="zip", root_dir=source)

def delete_old_files(backup_age, destination):
    backup_age = os.getenv('BACKUP_AGE', '1')
    destination= "/backups"
    os.system("find " + destination + " -mtime +60 -print")
    # get todays date, parse all the info

    # files_list = os.listdir(destination)
    # current_time = time.time()
    # for backup_files in files_list:
    #     file_path = os.path.join(destination, backup_files)
    #     if os.path.isfile(file_path):
    #         if (current_time - os.stat(file_path).st_birthtime) > backup_age * 86400:
    #             os.remove(file_path)

if __name__=="__main__":
    main()

