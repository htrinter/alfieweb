from pathlib import Path
from shutil import copyfile

CACHE_DIR_PATH = "generated-files/cache/"

def is_file_cached(format, layout, year, language):
    file_path = get_cache_file_path(format, layout, year, language)
    return file_path.is_file()

def get_cache_file_path(format, layout, year, language):
    file_name = get_cache_file_name(format, layout, year, language)
    return Path(CACHE_DIR_PATH + file_name)

def get_cache_file_name(format, layout, year, language):
    return "diary-{}-{}-{}-{}.pdf".format(format, layout, year, language)

def copy_to_cache(source_file_path, cache_file_name):
    cache_file_path = CACHE_DIR_PATH + cache_file_name
    copyfile(source_file_path, cache_file_path)
    return cache_file_path

def get_cache_dir_path():
    return CACHE_DIR_PATH
