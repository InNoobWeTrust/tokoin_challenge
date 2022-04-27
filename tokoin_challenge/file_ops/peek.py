from io import TextIOWrapper


def peekline(file_handle: TextIOWrapper) -> str:
    pos = file_handle.tell()
    line = file_handle.readline()
    file_handle.seek(pos)
    return line


