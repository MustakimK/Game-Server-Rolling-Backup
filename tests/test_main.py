import pytest
import time
import os

from game_server_rolling_backup.main import convert_to_seconds
from game_server_rolling_backup.main import backup_data
from game_server_rolling_backup.main import delete_old_files


def test_convert_to_seconds_pass():
    assert 1 == convert_to_seconds('1s')
    assert 60 == convert_to_seconds('1m')
    assert 7200 == convert_to_seconds('2h')
    assert 172800 == convert_to_seconds('2d')
    assert 604800 == convert_to_seconds('1w')


@pytest.mark.xfail
def test_convert_to_seconds_fail():
    convert_to_seconds('1')


def test_backup_data_pass(fs):
    save_dir = '/saves'
    backup_dir = '/backups'
    fs.create_dir(save_dir)
    fs.create_dir(backup_dir)

    assert len(os.listdir(backup_dir)) == 0

    fs.create_file('/saves/save.txt')
    backup_data(save_dir, backup_dir)

    backed_up_file = os.listdir(backup_dir)[0]
    assert backed_up_file.endswith('.zip')


def test_delete_old_files_deleted(fs):
    backup_dir = '/backups'
    file = fs.create_file(os.path.join(backup_dir, 'save.zip'))
    file.st_mtime = time.time() - 61

    assert len(os.listdir(backup_dir)) == 1
    delete_old_files(backup_dir, 60)
    assert len(os.listdir(backup_dir)) == 0


def test_delete_old_files_not_deleted(fs):
    backup_dir = '/backups'
    fs.create_file(os.path.join(backup_dir, 'save.zip'))

    assert len(os.listdir(backup_dir)) == 1
    delete_old_files(backup_dir, 60)
    assert len(os.listdir(backup_dir)) == 1
