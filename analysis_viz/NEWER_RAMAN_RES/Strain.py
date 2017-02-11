import numpy as np
import matplotlib.pyplot as plt

nostrain = "blyp_FREQS.txt"
strain = "1pblyp_FREQS.txt"

ns = np.genfromtxt(nostrain)
es = np.genfromtxt(strain)

nwmask = np.isfinite(ns)
esmask = np.isfinite(es)

markers = ['s', 'o', 'v', 'x', '+', '>']
harmonics = [r'$1^{st}$', r'$2^{nd}$', r'$3^{rd}$']
#plt.figure(figsize=(7,6))
plt.figure()
plt.title("Longitudinal Optical (and like) Modes")
plt.ylabel(r'$\omega \, (cm^{-1})$', fontsize=16)
plt.xlabel("Number of carbon atoms", fontsize=12)
plt.xlim([1,50])
plt_lines = []
for column in range(1,4):
    NW, = plt.plot(ns[:,0], ns[:,column], marker=markers[column-1], color="black")
    QE, = plt.plot(es[:,0], es[:,column], marker=markers[column-1], color="red")
    plt_lines.append([NW, QE])

legend1 = plt.legend(plt_lines[0], ["no strain", "1% strain"], loc=1)
plt.legend([l[0] for l in plt_lines], harmonics ,loc=3)
plt.gca().add_artist(legend1)

plt.grid(True)
plt.savefig("strain.png", dpi=300)
plt.show()
