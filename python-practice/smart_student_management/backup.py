import shutil
import os

# Current project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database path
DB_PATH = os.path.join(BASE_DIR, "students.db")

# Backup file
BACKUP_PATH = os.path.join(BASE_DIR, "students_backup.db")


# ---------------- BACKUP ----------------

def backup_database():

    try:

        shutil.copy(DB_PATH, BACKUP_PATH)

        print("\n✅ Database Backup Created Successfully!")
        print(f"📁 Backup File : {BACKUP_PATH}")

    except FileNotFoundError:

        print("\n❌ Database Not Found!")

    except Exception as e:

        print("\n❌ Backup Failed!")
        print(e)


# ---------------- RESTORE ----------------

def restore_database():

    try:

        shutil.copy(BACKUP_PATH, DB_PATH)

        print("\n✅ Database Restored Successfully!")

    except FileNotFoundError:

        print("\n❌ Backup File Not Found!")

    except Exception as e:

        print("\n❌ Restore Failed!")
        print(e)