from subprocess import Popen, PIPE, STDOUT
import os


with open(r'in.txt') as infile:
    script, file = map(lambda x: x.strip(), infile.readlines())

cur_dir = os.getcwd()
scr_spl = script.rsplit('/', 1)

if len(scr_spl) == 1:
    command = os.path.join(cur_dir, scr_spl[0])
else:
    command = script

with open(file) as stdin:
    try:
        proc = Popen([command], stdin=stdin, stdout=PIPE, stderr=STDOUT,  cwd='./', text=True)
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
