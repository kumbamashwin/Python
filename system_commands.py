#subprocess is the library used to invoke system commands

import subprocess
import os

if os.name == "nt":
    command  = "dir"
elif os.name == "posix":
    command ="ls"
    
output = subprocess.getoutput(command)
print(output)