import logging
import os
from collections import deque

from folder_storage.folder import Folder
from garbage_bak_collector import GarbageBakCollector

logging.basicConfig(level=logging.DEBUG)
all_folders = set()
tasks = deque()


async def remove_files(files: set):
    for file in files:
        os.remove(file)
        await logging.info(f'"{file}" file was removed!')


async def get_folders():


def event_loop(folder: Folder, is_removable_dir=False):
    if folder.is_empty() and is_removable_dir:
        os.rmdir(folder.path)
        logging.info(f'"{folder}" empty folder was removed!')
        return
    garbage_bak_collector = GarbageBakCollector(folder.get_list_files())
    tasks.append(folder.folders())
    tasks.append(garbage_bak_collector.garbage_bak_files())
    while tasks:
        task = tasks.pop(0)


if __name__ == '__main__':
    import args_parser
    garbage_bak_files = set()
    root_folder = Folder(args_parser.path)
    # main(root_folder, is_removable_dir=args_parser.is_removable_dir)
