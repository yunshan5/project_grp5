## import Path from pathlib into filetouch.py
from pathlib import Path


def create(filename):
    """
    this function will create a file with the name as the parenthesis
    """

    ## create a file path with the assigned file as the parenthesis of this
    # function
    fp_write = Path.cwd() / filename
    ## using .touch() create the file into the file path, fp_write.
    fp_write.touch()
