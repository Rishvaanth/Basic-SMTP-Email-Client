import subprocess

# subprocess.run("ls -la", shell=True) # !!security risk!!

# lsTest = subprocess.run(["ls", "-la"], capture_output=True, text=True)  #text gives the regular output instead of
# byte output.

lsTest = subprocess.run(["dig", "mx", "zoho.com"], capture_output=True, text=True)
getServer = subprocess.run(["grep", "SERVER"], capture_output=True, text=True, input=lsTest.stdout)
# print("the output is:")
print(lsTest.stdout)
indexa = getServer.stdout.rfind("(")
indexb = getServer.stdout.rfind(")")
# print(indexa)
# print(getServer.stdout)

serverAddress = getServer.stdout[indexa+1:indexb]
print(serverAddress)
