import os

def rename_files():
    # 1) get file names from a folder
    file_list = os.listdir(r"/Users/josepho/Desktop/prank/With Numbers/prank")
    os.chdir(r"/Users/josepho/Desktop/prank/With Numbers/prank")

    # 2) for each file, rename files
    for filename in file_list: # work with each file one at a time
        print("Old file name: " + filename)
        print("New file name: " + filename.translate(None, "0123456789"))
        os.rename(filename, filename.translate(None, "0123456789")) 
        
rename_files()
