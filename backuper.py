import os
import shutil
from datetime import date, datetime


def backup():
    """
    Does the backup.

    Returns:
        boolean: True if backup was successfull. False otherwise.
    """
    TODAY = date.today().strftime('%d-%m-%Y')
    CP_SAVES_FOLDER = './Cyberpunk 2077'
    BACKUP_DESTINATION = f'AutoBackup-{TODAY}'
    try:
        walk_to_root()
        LAST_SAVE_MTIME = os.stat(CP_SAVES_FOLDER).st_mtime
        CP_BACKUPS_FOLDERS = sort_backups()
        LAST_BACKUP_CTIME = os.stat(CP_BACKUPS_FOLDERS[0]).st_ctime
        if (is_backup_needed(CP_SAVES_FOLDER, CP_BACKUPS_FOLDERS)):
            shutil.copytree(CP_SAVES_FOLDER, BACKUP_DESTINATION)
            print(f'Cyberpunk {TODAY} saves backup successfull!')
        else:
            print(f'No new saves, no backup needed.\nNewest save date: {datetime.fromtimestamp(LAST_SAVE_MTIME)}.\nNewest backup date: {datetime.fromtimestamp(LAST_BACKUP_CTIME)}')
    except OSError as error:
        print(error.strerror)


def sort_backups():
    """
    Sorts existing backup folders by creation date in descending order. 

    Returns:
        array: Sorted array of saves folders in the Cyberpunk 2077 folder.
    """
    try:
        return sorted(next(os.walk("./"))[1], key=os.path.getmtime, reverse=True)
    except OSError as error:
        raise error


def walk_to_root():
    """
    Sets working directory context to the Cyberpunk 2077 saves folder (if backuper.py was placed correctly)
    """
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

def is_backup_needed(CP_SAVES_FOLDER, CP_BACKUPS_FOLDERS):
    """
    Compares last save modification date with most recent backup date.

    Returns:
        boolean: True if there is any new save to backup. False otherwise.
    """
    try:
        return os.stat(CP_SAVES_FOLDER).st_mtime > os.stat(CP_BACKUPS_FOLDERS[0]).st_ctime
    except OSError as error:
        raise error

# todo - add optional removal of old backups within given interval
# def remove_old_backups(TODAY,older_than_in_days=7):
#     try:
#         shutil.rmtree(f'./AutoBackup-{TODAY}')
#     except OSError as error:
#         raise error


backup()
