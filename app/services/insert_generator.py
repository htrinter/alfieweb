import os
import tempfile
import subprocess
from shutil import copyfile, rmtree

from services.insert_cache_manager import copy_to_cache, get_cache_file_name

TMP_DIR_PATH = "generated-files/tmp"

def generate_file(format, layout, language, year):
    generation_directory = init_generation_directory()

    alfie_arg = "{}-{}-{}-{}-no-no-yes".format(format, layout, language, year)
    alfie_pdf_file_name = "diary-{}-{}-{}.pdf".format(format, year, language)
    subprocess.run(["python3", "alfie.py", alfie_arg], cwd=generation_directory, timeout=20)

    cache_file_name = get_cache_file_name(format, layout, year, language)
    cache_file_path = copy_to_cache(generation_directory + "/" + alfie_pdf_file_name, cache_file_name)

    delete_generation_directory(generation_directory)

def init_generation_directory():
    tmpdir = tempfile.mkdtemp(dir = TMP_DIR_PATH)
    copyfile("lib/Alfie/alfie.py", tmpdir + "/alfie.py")
    return os.getcwd() + "/" + tmpdir

def delete_generation_directory(dir):
    rmtree(dir)
