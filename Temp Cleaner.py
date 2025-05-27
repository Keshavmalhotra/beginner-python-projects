import shutil
paths= ["", ""]  # Enter the path between double quotes, and use / instead of \
for i in paths:
 try:
  shutil.rmtree(i)
 except PermissionError:
  continue
 except FileNotFoundError:
  continue
