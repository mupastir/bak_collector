import os

BAK_EXTENSION = 'bak'
DOC_EXTENSION = 'doc'


class GarbageBakCollector:

    __slots__ = ('files')

    def __init__(self, files):
        self.files: set = files

    def _get_all_bak_files(self):
        for file in self.files:
            if isinstance(file, str) \
                    & (file.rsplit('.', 1)[-1] == BAK_EXTENSION):
                yield file

    def garbage_bak_files(self):
        all_bak_files = self._get_all_bak_files()
        for b in all_bak_files:
            if not os.path.join(
                    b.rsplit('.', 1)[0], DOC_EXTENSION
            ) in self.files:
                yield b
