#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

lob='b-freq.txt'
lo1='03p-freq.txt'
lo2='1p-freq.txt'

base = np.loadtxt(lob,usecols=(0,1))
st1 = np.loadtxt(lo1,usecols=(0,1))
st2 = np.loadtxt(lo2,usecols=(0,1))

w_b1 = ( st1[:,1] - base[:,1] )
w_b2 = ( st2[:,1] - base[:,1] )


def consec_change(in_array, out_array):
        for i in range(len(in_array)):
                if i>0 :
                        out_array[i-1] = (in_array[i] - in_array[i-1])

d1 = np.zeros(shape=(len(base)-1,1))
d2 = np.zeros(shape=(len(base)-1,1))
d3 = np.zeros(shape=(len(base)-1,1))
consec_change(base[:,1], d1)
consec_change(st1[:,1], d2)
consec_change(st2[:,1], d3)


pdf_pages = PdfPages('multi-change.pdf')
plt.rc('text', usetex=False)
fig = plt.figure(figsize=(10,7))
plt.title("$\Delta \omega_{LO} = \omega_{LO} (strain) - \omega_{LO} (no \, strain)$", fontsize=25)
plt.plot(base[:,0], w_b1, label="0.3% strain", color='black', lw=2, ls='-', marker='.', ms=15)
plt.plot(base[:,0], w_b2, label="1.0% strain", color='red', lw=2, ls='-', marker='.', ms=15)
plt.xlabel("n", fontsize=20)
plt.ylabel("$\Delta \Omega_{LO}$ (cm$^{-1}$)", fontsize=20)
plt.tick_params(axis='both', labelsize=20)
plt.legend(loc='best', fancybox=True)
pdf_pages.savefig(fig)
pdf_pages.close()

pdf_pages = PdfPages('single-change.pdf')
plt.rc('text', usetex=False)
fig = plt.figure(figsize=(10,7))
plt.title("$\Delta \omega_{LO} = \omega_{LO} (n+1) - \omega_{LO} (n)$", fontsize=25)
plt.plot(base[1:,0], d1, label="no strain", color='black', lw=2, ls='-', marker='.', ms=15)
plt.plot(base[1:,0], d2, label="0.3% strain", color='blue', lw=2, ls='-', marker='.', ms=15)
plt.plot(base[1:,0], d3, label="1.0% strain", color='red', lw=2, ls='-', marker='.', ms=15)
plt.xlabel("n", fontsize=20)
plt.ylabel("$\Delta \omega_{LO}$ (cm$^{-1}$)", fontsize=20)
plt.tick_params(axis='both', labelsize=20)
plt.legend(loc='best', fancybox=True)
pdf_pages.savefig(fig)
pdf_pages.close()

