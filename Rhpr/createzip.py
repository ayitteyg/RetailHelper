import os
import shutil
from os import path
from zipfile import ZipFile
from shutil import make_archive

def main():

    shutil.make_archive("RetailHelper", 'zip', "Rhpr")
    #shutil.make_archive("RetailHelper", 'zip', "Rhpr")

if __name__ =="__main__":
    main()