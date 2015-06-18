import os, shutil
import ctypes.wintypes

CSIDL_PERSONAL = 5       # My Documents
SHGFP_TYPE_CURRENT = 1   # Want current, not default value

buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

my_documents = buf.value

d = os.path.join(my_documents, 'LabVIEW Data', 'Quick Drop Plugins')

shutil.copytree("Show Open VIs", os.path.join(d, "Show Open VIs"))      # creates the dir(s) if necessary
shutil.copy2("Show Open VIs.vi", d)
