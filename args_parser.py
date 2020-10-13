import argparse

APPLICATION_DESCRIPTION = '''Look through the path and remove empty folders 
and not relevant *.bak files.'''
PATH_ARG_HELP_TEXT = 'Path to folder from which ' \
                     'is needed to collect *.bak files.'

parser = argparse.ArgumentParser(description=APPLICATION_DESCRIPTION)
parser.add_argument('path', help=PATH_ARG_HELP_TEXT, default=None)
parser.add_argument('-df', '--delete-folder', action='store_true')
args = parser.parse_args()
path, is_removable_dir = args.path, args.delete_folder
