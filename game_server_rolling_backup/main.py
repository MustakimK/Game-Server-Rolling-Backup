import os
import time
from datetime import datetime
import shutil

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

DEFAULT_BACKUP_FREQUENCY = '20m'
DEFAULT_OLDEST_BACKUP_AGE = '1w'
DEFAULT_SAVE_DIR = '/saves'
DEFAULT_BACKUP_DIR = '/backups'

UNITS_IN_SECONDS = {'w': 604800, 'd': 86400, 'h': 3600, 'm': 60, 's': 1}


def main():
    backup_frequency = os.getenv('BACKUP_FREQUENCY', DEFAULT_BACKUP_FREQUENCY)
    max_age = os.getenv('OLDEST_BACKUP_AGE', DEFAULT_OLDEST_BACKUP_AGE)
    save_dir = os.getenv('SAVE_DIR', DEFAULT_SAVE_DIR)
    backup_dir = os.getenv('BACKUP_DIR', DEFAULT_BACKUP_DIR)

    log.info(
        f'Starting backups from {save_dir} to {backup_dir} with interval {backup_frequency} and max age {max_age}')

    backup_frequency = convert_to_seconds(backup_frequency)
    max_age_seconds = convert_to_seconds(max_age)

    if (backup_frequency > max_age_seconds):
        error_msg = 'OLDEST_BACKUP_AGE must be greater than BACKUP_FREQUENCY'
        log.error(error_msg)
        raise Exception(error_msg)

    while(True):
        backup_data(save_dir, backup_dir)
        delete_old_files(backup_dir, max_age_seconds)
        time.sleep(backup_frequency)


def backup_data(source_dir, destination_dir):
    filename = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    format = 'zip'

    log.info(f'Creating backup: {filename}.{format}')
    shutil.make_archive(
        base_name=os.path.join(destination_dir, filename),
        format=format,
        root_dir=source_dir)


def delete_old_files(backup_dir, max_age_seconds):
    list_of_files = os.listdir(backup_dir)
    current_time = time.time()

    for filename in list_of_files:
        path = os.path.join(backup_dir, filename)
        file_mtime = os.path.getmtime(path)

        if (current_time - file_mtime) > max_age_seconds:
            log.info(
                f'Removing old backup: {filename} modified at {file_mtime}')
            os.remove(path)


def convert_to_seconds(time_string):
    units = time_string[-1]
    if units not in UNITS_IN_SECONDS:
        error_msg = f'Invalid units in time string: {time_string}'
        log.error(error_msg)
        raise Exception(error_msg)

    try:
        time_int = int(time_string[:-1])
        return time_int * UNITS_IN_SECONDS[units.lower()]
    except Exception:
        error_msg = f'Failed to parse time string: {time_string}'
        log.error(error_msg)
        raise Exception(error_msg)


if __name__ == "__main__":
    main()
