import subprocess
import os

# Define the path to the Blender executable
blender_executable_path = 'D:/Program Files/Blender Foundation/Blender 4.0/blender.exe'


blend_file_path = './basicWood.blend'
script_path = './blenderScript.py'

# Your CMD 
command = f'"{blender_executable_path}" -b "{blend_file_path}" -P "{script_path}"'

# Run in subprocess
process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Output
print('OUT:', process.stdout)
print('ERR:', process.stderr)


# open the rendered image
os.system(f'start imageOut.png')
