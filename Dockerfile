FROM python:3.10

ADD run.py /

# RUN pip install os
# RUN pip install 

CMD ["python3", "-u" , "./run.py"]

# Take folder X, zip it up, put it in backups folder with timestamp every 5 minutes, Delete any backups older than a day, Backup that folder to NFS
# Need crontab too
# NFS part - -https://itenterpriser.com/how-to/how-to-setup-truenas-core-and-connect-to-it-from-ubuntu/
