import subprocess

with open(r'in.txt') as infile:
    command = infile.readline()

with open(r'out.txt', 'w') as f:
    proc = subprocess.Popen([command], stdout=f)
    proc.communicate()
