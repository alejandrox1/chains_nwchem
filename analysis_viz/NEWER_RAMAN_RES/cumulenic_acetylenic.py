import numpy as np
import matplotlib.pyplot as plt

polyyne ="b-freq.txt"
cumulenic="FREQSeven.txt"

nw = np.genfromtxt(polyyne, usecols=(0,1))
es = np.genfromtxt(cumulenic, usecols=(0,1))

nwmask = np.isfinite(nw)
esmask = np.isfinite(es)

markers = ['s', 'o', 'v', 's', '+', '>']
harmonics = [r'$1^{st}$', r'$2^{nd}$', r'$3^{rd}$']
plt.figure()
plt.title("Longitudinal Optical Mode")
plt.ylabel(r'$\omega \, (cm^{-1})$', fontsize=16)
plt.xlabel("Number of carbon atoms", fontsize=12)
plt.xlim([1,50])
plt_lines = []
for column in range(1,2):
    NW, = plt.plot(nw[:,0], nw[:,column], marker=markers[column-1], color="black")
    QE, = plt.plot(es[:,0], es[:,column], marker=markers[column-1], color="red")
    plt_lines.append([NW, QE])

legend1 = plt.legend(plt_lines[0], ["Acetylenic", "Cumulenic"], loc=1)
#plt.legend([l[0] for l in plt_lines], harmonics ,loc=3)
plt.gca().add_artist(legend1)

plt.grid(True)
plt.savefig("polyyne_cumulene.png", dpi=300)
plt.show()
