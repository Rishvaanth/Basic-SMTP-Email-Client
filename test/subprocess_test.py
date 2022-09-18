import os
import subprocess

os.system("echo Hello there!")
# dig_output = os.system("dig mx uwm.edu")

# listfiles = subprocess.run(["ls", "-l"])

dig_uwm = subprocess.run(["dig", "mx", "uwm.edu"], stdout=subprocess.PIPE)

print(dig_uwm.stdout)
