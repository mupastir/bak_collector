import logging
import os
from collections import deque
from typing import Deque, List

import asyncio

import args_parser
from folder_storage.folder import Folder
from garbage_bak_collector import GarbageBakCollector

logging.basicConfig(level=logging.DEBUG)


async def remove_files(file_to_remove):
    os.remove(file_to_remove)
    logging.info(f'"{file_to_remove}" file was removed!')


async def remove_dir(path_dir_to_remove):
    os.rmdir(path_dir_to_remove)
    logging.info(f'"{path_dir_to_remove}" folder was removed!')


async def collect_bak_files(folder_files: List[str]):
    garbage_bak_collector = GarbageBakCollector(folder_files)
    garbage_bak_files = garbage_bak_collector.garbage_bak_files
    for garbage_bak_file in garbage_bak_files:
        await remove_files(garbage_bak_file)


async def collect_all_files(folder: Folder):
    folder_files = folder.get_list_files()
    await collect_bak_files(folder_files)
    if args_parser.is_removable_dir and folder.is_empty:
        await remove_dir(folder.path)


async def main():
    root_folder = Folder(args_parser.path)
    folders = deque(root_folder.nested_folders())
    tasks = []
    for folder in folders:
        task = asyncio.create_task(collect_all_files(folder))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
