import os
import shutil  #importing to delete all files in directory

if not os.path.exists('python cg'):
    os.mkdir("python cg") # to create directory

os.rmdir("python cg")  #To remove empty directory

#shutil.rmtree('python cg')

print(os.getcwd())
print(os.listdir())

os.chdir("cg")
os.chdir("..")
