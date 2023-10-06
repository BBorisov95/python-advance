from os.path import dirname, abspath
import os

DIRECTORY = abspath(dirname(dirname(__file__)))


files = {}


def recursive_dir_crawler(starting_point, levels_to_crawl):
    for element in os.listdir(starting_point):
        target = os.path.join(starting_point, element)
        if os.path.isfile(target):
            file_ext = element.split('.')[-1]
            if file_ext not in files:
                files[file_ext] = []
            files[file_ext].append(element)
        else:
            recursive_dir_crawler(target, levels_to_crawl - 1)



recursive_dir_crawler(DIRECTORY, 1)

with open(os.path.join(DIRECTORY, 'output.txt'), 'w') as f:
    for file_extension, file_names in sorted(files.items()):
        f.write(f'.{file_extension}\n')
        for f_name in file_names:
            f.write(f'- - - {f_name}\n')

