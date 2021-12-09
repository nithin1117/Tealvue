import shutil

original = r'original path where the directory is currently stored\directory name'
target = r'target path where the directory will be moved\directory name'

# original = input()
# target = input()

shutil.move(original,target)
