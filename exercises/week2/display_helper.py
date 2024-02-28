import pywt
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def plot_haar_coeffs(data, title, levels=5):
    """Show dwt coefficients for given data ."""
    w = pywt.Wavelet('haar')
    a = data
    ca = []
    cd = []

    mode = pywt.Modes.sp1DWT = 1
    for i in range(levels):
        (a, d) = pywt.dwt(a, w, mode)
        ca.append(a)
        cd.append(d)

    fig = plt.figure()
    ax_main = fig.add_subplot(len(ca) + 1, 1, 1)
    ax_main.set_title(title)
    ax_main.plot(data)
    ax_main.set_xlim(0, len(data) - 1)

    for i, x in enumerate(ca):
        ax = fig.add_subplot(len(ca) + 1, 2, 3 + i * 2)
        ax.plot(x, 'r')
        ax.set_ylabel("A%d" % (i + 1))

        ax.set_xlim(0, len(x) - 1)
        

    for i, x in enumerate(cd):
        ax = fig.add_subplot(len(cd) + 1, 2, 4 + i * 2)
        ax.plot(x, 'g')
        ax.set_ylabel("D%d" % (i + 1))
        # Scale axes
        ax.set_xlim(0, len(x) - 1)
        
        ax.set_ylim(min(0, 1.4 * min(x)), max(0, 1.4 * max(x)))
    fig.subplots_adjust(left=0.2, right=1.5, top=1.9, bottom=0.1)   