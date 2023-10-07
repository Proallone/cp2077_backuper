import os
import shutil 
from datetime import date, datetime 

ROOT = os.path.abspath( os.path.dirname( __file__ ) )
os.chdir(ROOT)

CP_SAVES_FOLDER = './Cyberpunk 2077'
CP_BACKUPS_FOLDERS = sorted(next(os.walk("./"))[1], key=os.path.getmtime, reverse=True)

LAST_SAVE_MTIME = os.stat(CP_SAVES_FOLDER).st_mtime
LAST_BACKUP_CTIME = os.stat(CP_BACKUPS_FOLDERS[0]).st_ctime

TODAY = date.today().strftime('%d-%m-%Y')
BACKUP_DESTINATION = f'AutoBackup-{TODAY}'

def make_backup():
    try:
        if(is_backup_needed()):
            shutil.copytree(CP_SAVES_FOLDER, BACKUP_DESTINATION)
            print(f'Cyberpunk {TODAY} saves backup successfull!')
        else:
            print(f'No new saves, no backup needed.\nNewest save date: {datetime.fromtimestamp(LAST_SAVE_MTIME)}.\nNewest backup date: {datetime.fromtimestamp(LAST_BACKUP_CTIME)}')
    except OSError as error:
        print(error) 
    
def is_backup_needed ():
    if(LAST_SAVE_MTIME > LAST_BACKUP_CTIME):
        return True
    else:
        return False

make_backup()
