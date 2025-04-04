import shutil
import os
import sys

SRC_FILE = "./pywerviewjson-main.py"
TARGET_FILE = "/usr/lib/python3/dist-packages/pywerview/cli/main.py"
BACKUP_FILE = f"{TARGET_FILE}.orig"

def backup_and_copy():
    if not os.path.exists(TARGET_FILE):
        print(f"Target file '{TARGET_FILE}' does not exist.")
        return

    if os.path.exists(BACKUP_FILE):
        print(f"Backup already exists at '{BACKUP_FILE}'.")
    else:
        shutil.copy2(TARGET_FILE, BACKUP_FILE)
        print(f"Backup created at '{BACKUP_FILE}'.")

    shutil.copy2(SRC_FILE, TARGET_FILE)
    print(f"'{SRC_FILE}' has been copied to '{TARGET_FILE}'.")

def restore_original():
    if not os.path.exists(BACKUP_FILE):
        print(f"Backup file '{BACKUP_FILE}' does not exist. Cannot restore.")
        return

    shutil.copy2(BACKUP_FILE, TARGET_FILE)
    os.remove(BACKUP_FILE)
    print(f"Original file restored from '{BACKUP_FILE}' to '{TARGET_FILE}'. Backup removed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py [copy|restore]")
        sys.exit(1)

    action = sys.argv[1].lower()

    if action == "copy":
        backup_and_copy()
    elif action == "restore":
        restore_original()
    else:
        print("Invalid argument. Use 'copy' or 'restore'.")
