from subprocess import Popen, PIPE, STDOUT
import os

envs = os.environ
with open(r'in.txt') as infile:
    script = infile.readline().strip()
    for line in infile:
        k, v = line.split()
        envs[k] = v

try:
    proc = Popen([script], stdout=PIPE, stderr=STDOUT,  cwd='./', text=True, env=envs)
    out, err = proc.communicate()
    if proc.returncode != 0:
        print(f'Warning: {script} returned a non-zero exit code', file=open('err.txt', 'w'))
    else:
        print('', file=open('err.txt', 'w+'))

except OSError as e:
    err = f'Failed to run programm {script}'
    print(err, file=open('err.txt', 'w'))
else:
    print(out, file=open('out.txt', 'w+'))