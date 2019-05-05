import glob

for filename in glob.iglob('./**/*.c', recursive=True):
    print(filename)

# Test Case:
# Please run this in separate directory with files
