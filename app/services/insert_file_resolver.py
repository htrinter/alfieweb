from flask import send_from_directory

from services.insert_cache_manager import is_file_cached, get_cache_file_name, get_cache_dir_path
from services.insert_generator import generate_file

def get_file(format, layout, language, year):
    if is_file_cached(format, layout, year, language) == False:
        generate_file(format, layout, language, year)

    cache_file_name = get_cache_file_name(format, layout, year, language)
    return send_from_directory(get_cache_dir_path(), cache_file_name)
