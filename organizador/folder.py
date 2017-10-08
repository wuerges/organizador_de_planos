import tempfile
from zipfile import ZipFile
from contextlib import contextmanager
import ezodf


def find_name(zipfile, name):
    with tempfile.NamedTemporaryFile() as temp:
        with zipfile.open(name, 'r') as f:
            temp.write(f.read())
        #doc = ezodf.opendoc(f.name)
        return "_" + f.name





def move_file(old_zip, new_zip, old_name, new_name):
    with old_zip.open(old_name, 'r') as old_file:
        with new_zip.open(new_name, 'w') as new_file:
            new_file.write(old_file.read())

def rezipFolder(old_path, new_path):
    with ZipFile(new_path, 'w') as new_zip:
        with ZipFile(old_path, 'r') as old_zip:
            for name in old_zip.namelist():
                move_file(old_zip, new_zip, name, "_" +name)


rezipFolder("a.zip", "b.zip")
