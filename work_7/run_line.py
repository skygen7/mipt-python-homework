from subprocess import Popen, PIPE, STDOUT, TimeoutExpired
import shlex

with open(r'in.txt') as infile:
    command = infile.readline().strip()

com_split = shlex.split(command)

script = com_split[0]
try:
    proc = Popen(com_split, stdout=PIPE, stderr=STDOUT,  cwd='./', text=True)
    try:
        out, err = proc.communicate(timeout=0.5)
        if proc.returncode != 0:
            print(f'Warning: {script} returned a non-zero exit code', file=open('err.txt', 'w'))
        else:
            print('', file=open('err.txt', 'w+'))
    except TimeoutExpired as te:
        proc.kill()
        out, err = proc.communicate()
        print(f'Timeout expired for program {script}', file=open(r'err.txt', 'w'))
except OSError as e:
    err = f'Failed to run programm {script}'
    print(err, file=open('err.txt', 'w'))
else:
    print(out, file=open('out.txt', 'w+'))
