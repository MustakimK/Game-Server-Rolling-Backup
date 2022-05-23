import os,time
from datetime import datetime
import shutil

while(True):
    backup_frequency = os.environ['BACKUP_FREQUENCY', 60]
    backup_age = os.environ['BACKUP_AGE',1]
    source = "/home/kaz/DockerFiles/saves"
    destination= "/home/kaz/DockerFiles/backups"
    fileName = datetime.now().strftime("%Y_%m_%d-%H_%M_%S_%p")

    shutil.make_archive(fileName, 'zip', source)
        
    files_list = os.listdir(destination)
    current_time = time.time()
    for backup_files in files_list:
        file_path = os.path.join(destination, backup_files)
        if os.path.isfile(file_path):
            if (current_time - os.stat(file_path).st_birthtime) > backup_age * 86400:
                os.remove(file_path)    
            
        print("test")

    time.sleep(backup_frequency*60)


