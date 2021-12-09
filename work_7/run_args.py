from subprocess import Popen, PIPE, STDOUT


with open(r'in.txt') as infile:
    command = [arg.strip('\n') for arg in infile if arg != '']

try:
    proc = Popen(command, stdout=PIPE, stderr=STDOUT)
    out, _ = proc.communicate()
except OSError as e:
    err = f'Failed to run programm {command[0]}'
    print(err, file=open('err.txt', 'w'))
else:
    print(out.decode(), file=open('out.txt', 'w+'))
    print('', file=open('err.txt', 'w+'))