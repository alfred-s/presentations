from subprocess import call
import os
from shutil import copyfile

# in order to run `.shrinkpdf.sh`, you have to give it 
# permission. Use
# chmod +x shrinkpdf.sh


origin = "./uncompressed_figures"
destination = "./figures"
files = os.listdir(origin)
for file in files:
    if file.endswith(".pdf"):
        replace = False
        old_file = os.path.join(origin, file)
        new_file = os.path.join(destination, file) 
        if os.path.exists(new_file):
            dt = os.path.getmtime(old_file) - os.path.getmtime(new_file)
            replace = (dt > 0) # Check whether file is older
        else: # if not there yet: create it
            replace = True
        if replace:
            if os.path.getsize(old_file) < 50000:
                copyfile(old_file, new_file)
            else:
                print(file)
                 ###Apply shrinkpdf.sh --- must be in the same directory! 
                string = "./shrinkpdf.sh " \
                    + old_file + " " + new_file
                os.system(string)

                
