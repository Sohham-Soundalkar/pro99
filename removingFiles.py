import os
import shutil
import time

def main():
    deletedFilesCount = 0
    deletedFoldersCount = 0
    path = '/path_to_delete'
    days = 30
    seconds = time.time()-(days*24*60*60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedFoldersCount += 1
                break

            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)

                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFoldersCount += 1

                for file in files:
                    file_path = os.path.join(root_folder, file)

                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deletedFilesCount += 1

        else:
            if seconds >= get_file_or_folder_age(path):
                remove_file(path)
                deletedFilesCount += 1

    else:
        print(f'"{path}" is not found')
        deletedFilesCount += 1

    print(f'Total folders deleted: {deletedFoldersCount}')
    print(f'Total files deleted: {deletedFilesCount}')