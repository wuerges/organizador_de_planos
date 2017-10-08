import tempfile
from zipfile import ZipFile
from contextlib import contextmanager
import ezodf
import re
import os

def find_turma(text):
    m = re.search(r'\d\d\d\d\d', text)
    if m:
        return m.group(0)
    return None

def find_name_body(body):
    text = "\n".join(span.plaintext() for span in body)
    #print(text)
    turma = find_turma(text)
    return find_turma(text) 

def find_name(zipfile, name):

    new_turma = None
    with tempfile.NamedTemporaryFile() as temp:
        with zipfile.open(name, 'r') as f:
            temp.write(f.read())
        try:
            #print("going to open",  temp.name)
            doc = ezodf.opendoc(temp.name)
            new_turma = find_name_body(doc.body)
            #print("odf file:", name)
            #print("plaintext", new_name)
        except KeyError:
            pass
            #print("not a odf file:", name)
            #new_name = None
    if new_turma:
        new_name = os.path.join(new_turma, name)
    else:
        new_name = os.path.join("sem_turma", name)
    print("new_name:", new_name)
    return new_name

def move_file(old_zip, new_zip, old_name, new_name):
    with old_zip.open(old_name, 'r') as old_file:
        with new_zip.open(new_name, 'w') as new_file:
            new_file.write(old_file.read())

def rezipFolder(old_path, new_path):
    with ZipFile(new_path, 'w') as new_zip:
        with ZipFile(old_path, 'r') as old_zip:
            for name in old_zip.namelist():
                new_name = find_name(old_zip, name)
                if new_name:
                    move_file(old_zip, new_zip, name, new_name)

