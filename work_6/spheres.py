class Spheres:

    FILE = r'out.txt'
    PI = 3.14

    def __init__(self, *args):
        self.radius, self.x, self.y, self.z = args
        self.volume = self.calculate_volume()
        self.run()

    def calculate_volume(self):
        volume = 4 / 3 * self.PI * self.radius ** 3
        return round(volume, 2)

    def run(self):
        kwargs = {
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'r': self.radius,
            'vol': self.volume
        }
        out = 'X: {x}\nY: {y}\nZ: {z}\nR: {r}\nVolume: {vol}'.format(**kwargs)

        print(out, file=open(self.FILE, 'w'))


with open(r'in.txt') as f:
    line = map(int, f.readline().split())
    sphere = Spheres(*line)
    sphere.run()
