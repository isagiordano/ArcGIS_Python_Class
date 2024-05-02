# 1. Simple directory tree
# Replicate this tree of directories and subdirectories:
#
# ├── draft_code
# |   ├── pending
# |   └── complete
# ├── includes
# ├── layouts
# |   ├── default
# |   └── post
# |       └── posted
# └── site
# Using os.system or os.mkdirs replicate this simple directory tree.
# Delete the directory tree without deleting your entire hard drive.

import os
file_path = r"C:\directory_tree_3" # on my own laptop using a c drive
os.mkdir(file_path)

#  add subdirectory
draft_code = r"C:\directory_tree_3\draft_code"
os.mkdir(draft_code)
pending = r"C:\directory_tree_3\draft_code\pending"
os.mkdir(pending)
complete = r"C:\directory_tree_3\draft_code\complete"
os.mkdir(complete)

includes = r"C:\directory_tree_3\includes"
os.mkdir(includes)

layouts = r"C:\directory_tree_3\layouts"
os.mkdir(layouts)
default = r"C:\directory_tree_3\layouts\default"
os.mkdir(default)
post = r"C:\directory_tree_3\layouts\post"
os.mkdir(post)
posted = r"C:\directory_tree_3\layouts\post\posted"
os.mkdir(posted)
#
site = r"C:\directory_tree_3\site"
os.mkdir(site)

import shutil

try:
    shutil.rmtree(file_path)
    print('Folder and its content removed')
except:
    print('Folder not deleted')

#  https://www.freecodecamp.org/news/python-delete-file-how-to-remove-files-and-folders/#:~:text=To%20delete%20a%20folder%20that%20has%20subfolders%20and%20files%20in,on%20the%20now%20empty%20folder.
# reference

