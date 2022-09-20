import subprocess

digtest = subprocess.Popen(["dig", "mx", "uwm.edu"], stdout=subprocess.PIPE)


print(digtest)
