from subprocess import Popen, PIPE, STDOUT


with open(r'in.txt') as infile:
    script = infile.readline().strip()
    args = [arg.strip('\n') for arg in infile if arg != '']

command = [script] + args

try:
    proc = Popen(command, stdout=PIPE, stderr=STDOUT,  cwd='./')
    out, err = proc.communicate()
    if proc.returncode != 0:
        print(f'Warning: {script} returned a non-zero exit code', file=open('err.txt', 'w'))
    else:
        print('', file=open('err.txt', 'w+'))

except OSError as e:
    err = f'Failed to run programm {script}'
    print(err, file=open('err.txt', 'w'))
else:
    print(out.decode(), file=open('out.txt', 'w+'))
