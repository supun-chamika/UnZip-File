# import the necessary modules!
import zipfile
from tkinter import Tk
from tkinter.filedialog import askopenfilename

print('Select zip file -> ')

# we don't want a full GUI, so keep the root window from appearing
Tk().withdraw()

# show an "Open" dialog box and return the path to the selected file
file = askopenfilename()

# display a start message
print('Starting to Unzip the File!')

# use ZipFile method
root = zipfile.ZipFile(file)

# give destination path
root.extractall('Extracted')
root.close()

# display the end message
print('Successfully Unzipped!')
