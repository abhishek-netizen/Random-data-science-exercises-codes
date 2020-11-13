import subprocess
import re
import webbrowser

myUrl = input("Enter url:")

ping = subprocess.Popen(
    ["ping",myUrl],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
    )
out, error = ping.communicate()
m = re.search('(\d+.\d+\.\d+\.\d+)', out)
ip = m.group(0)
print (out)

webbrowser.open(ip)
