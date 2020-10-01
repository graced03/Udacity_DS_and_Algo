# For this problem, the goal is to write code for finding all files under a directory 
# (and all directories beneath it) that end with ".c"
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    target_file_list = []
    path_list = []
    
    if len(os.listdir(path)) == 0:  # Stopping condition
        return []
    
    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isfile(item):
            if item.endswith("." + suffix):
                target_file_list.append(item)
        else:
            path_list.append(os.path.join(item))
    
    for path_item in path_list:
        target_file_list.extend(find_files(suffix, path_item))
    
    return target_file_list

# Testing
# Normal cases
print(find_files('h', './testdir/'))
# ['./testdir/t1.h', './testdir/subdir1/a.h', './testdir/subdir5/a.h', './testdir/subdir3/subsubdir1/b.h']
print(find_files('c', './testdir/'))
# ['./testdir/t1.c', './testdir/subdir1/a.c', './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c']

# Edge cases
print(find_files('', './testdir/'))
# []
print(find_files('z', './testdir/'))
# []