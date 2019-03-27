import arrow
import os
import mimetypes

def date_timeformat(date_str):
    return arrow.get(date_str).humanize()


def file_type(key):
    file_info = os.path.splitext(key)
    file_extension = file_info[1]
    try:
        return mimetypes.types_map[file_extension]
    except KeyError():
        return 'Unknown'
    except:
        return 'Unknown'