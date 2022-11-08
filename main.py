import gzip
import shutil


dir_name = r'/var/log'


def compress():
    """the function reads files in the directory and compresses them using the compression utility 'gzip'."""
    for file_name in dir_name:  # loop through items in dir
        with open(file_name, 'rb') as f_in:
            with gzip.open('log.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


if __name__ == '__main__':
    compress()







