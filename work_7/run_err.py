import subprocess

with open(r'in.txt') as infile:
    command = infile.readline()

try:
    proc = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
except OSError as e:
    err = f'Failed to run programm {command}'
    print(err, file=open('err.txt', 'w'))
else:
    print(out.decode(), file=open('out.txt', 'w+'))
    print(err.decode(), file=open('err.txt', 'w+'))
