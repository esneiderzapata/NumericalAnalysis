import matplotlib.pyplot as plt
from io import BytesIO
def grafica(points):
    for xpoints,ypoints in points:
        plt.plot(xpoints, ypoints)
    plt.xlabel('x')
    plt.ylabel('y')
    buf = BytesIO()
    plt.savefig(buf)
    plt.close()
    buf.seek(0)
    return buf