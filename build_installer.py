import os

# Build the executable
os.system("pyinstaller --onefile install.py")

# Rename the executable file
original_name = "dist/install.exe"
new_name = "dist/Lingua_Franca_install.exe"
os.rename(original_name, new_name)
