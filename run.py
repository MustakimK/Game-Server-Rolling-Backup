import os,time
from datetime import datetime
import shutil

def main():
    backup_frequency = os.getenv('BACKUP_FREQUENCY', '60')
    backup_age = os.getenv('BACKUP_AGE', '1')
    source = os.getenv('VOL_SRC', '/saves')
    destination= os.getenv('VOL_DST', '/backups')

    while(True):
        
        fileName = datetime.now().strftime("%Y_%m_%d-%H_%M_%S_%p")

        backup_data(destination, fileName, source)
        delete_old_files(backup_age, destination)  
        time.sleep(int(backup_frequency)*60)

def backup_data(destination, fileName, source):
    shutil.make_archive(base_name=(os.path.join(destination,fileName)), format="zip", root_dir=source)

def delete_old_files(backup_age, destination):

    list_of_files = os.listdir(destination)

    for filename in list_of_files:

        path = os.path.join(destination, filename)

        modified_time=os.path.getmtime(path)
        if time.time()-modified_time > (backup_age * 86400): #time in seconds
            os.remove(path)
            
if __name__=="__main__":
    main()

#unit tests, support units, make constants 