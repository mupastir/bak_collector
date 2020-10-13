import os


class Folder:
    __slots__ = ('path')

    def __init__(self, path):
        if not os.path.isdir(path):
            raise IsADirectoryError(f'"{self.path}" - not found such directory')
        self.path: str = path

    def __repr__(self):
        return self.path

    def is_empty(self):
        return len(os.listdir(self.path)) == 0

    def get_list_files(self):
        return [os.path.join(self.path, f) for f in os.listdir(self.path)
                if os.path.isfile(os.path.join(self.path, f))]

    def folders(self):
        return [Folder(path=os.path.join(self.path, d))
                for d in os.listdir(self.path)
                if os.path.isdir(os.path.join(self.path, d))]
