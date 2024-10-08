import argparse
import matplotlib.pyplot as plt
import numpy
import os
import pickle

def plot(d0_0,d1250_0,d1250_1,d1250_2,d2500_0,d2500_1,d2500_2,d5000_0,d5000_1):
    plt.rcParams['text.usetex'] = True
    plt.rcParams.update({'font.size': 48})
    plt.rcParams['lines.linewidth'] = 8
    plt.ioff()
    fig,ax = plt.subplots(figsize=(16.5,12.3))
    ts = d1250_0[-1]
    COL3 = '#FFBA08'
    COL2 = '#F48C06'
    COL1 = '#DC2F02'
    COL0 = '#9D0208'
    COLWHITE = '#F7F7F8'
    COLBLACK = '#001134'
    fig.set_tight_layout(True)
    ax.plot(ts,numpy.sqrt(d0_0[1]),c=COL0,label="0",linestyle='dashed')
    ax.plot(ts,numpy.sqrt(d1250_0[1]),c=COL1,label="1250")
    ax.plot(ts,numpy.sqrt(d1250_1[1]),c=COL1)
    ax.plot(ts,numpy.sqrt(d1250_2[1]),c=COL1)
    ax.plot(ts,numpy.sqrt(d2500_0[1]),c=COL2,label="2500")
    ax.plot(ts,numpy.sqrt(d2500_1[1]),c=COL2)
    ax.plot(ts,numpy.sqrt(d2500_2[1]),c=COL2)
    ax.plot(ts,numpy.sqrt(d5000_0[1]),c=COL3,label="5000")
    ax.plot(ts,numpy.sqrt(d5000_1[1]),c=COL3)
    ax.legend(fontsize=20,loc="upper left",title="no. GMCs")
    ax.set_xlim(0,1)
    ax.spines[['right', 'top']].set_visible(False)
    ax.set_xlabel("time $t$ (Gyr)")
    ax.set_ylabel(r'velocity dispersion $\sigma$ (km s${}^{-1}$)')
    ax.tick_params(axis='x', colors=COLWHITE)
    ax.tick_params(axis='y', colors=COLWHITE)
    ax.yaxis.label.set_color(COLWHITE)
    ax.xaxis.label.set_color(COLWHITE)
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(8)
        ax.spines[axis].set_color(COLWHITE)
    ax.tick_params(width=8)
    plt.savefig("figure_sigma.svg",dpi=600,transparent=True)
    plt.savefig("figure_sigma.png",dpi=600,transparent=True)
    plt.close()

def main():
    parser = argparse.ArgumentParser("plot_gmc_angular")
    parser.add_argument("d0_0")
    parser.add_argument("d1250_0")
    parser.add_argument("d1250_1")
    parser.add_argument("d1250_2")
    parser.add_argument("d2500_0")
    parser.add_argument("d2500_1")
    parser.add_argument("d2500_2")
    parser.add_argument("d5000_0")
    parser.add_argument("d5000_1")
    args = parser.parse_args()
    if os.path.exists(args.d0_0):
        with open(args.d0_0,"rb") as file:
            d0_0 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d1250_0):
        with open(args.d1250_0,"rb") as file:
            d1250_0 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d1250_1):
        with open(args.d1250_1,"rb") as file:
            d1250_1 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d1250_2):
        with open(args.d1250_2,"rb") as file:
            d1250_2 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d2500_0):
        with open(args.d2500_0,"rb") as file:
            d2500_0 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d2500_1):
        with open(args.d2500_1,"rb") as file:
            d2500_1 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d2500_2):
        with open(args.d2500_2,"rb") as file:
            d2500_2 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d5000_0):
        with open(args.d5000_0,"rb") as file:
            d5000_0 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d5000_1):
        with open(args.d5000_1,"rb") as file:
            d5000_1 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    plot(d0_0,d1250_0,d1250_1,d1250_2,d2500_0,d2500_1,d2500_2,d5000_0,d5000_1)

if __name__ == "__main__":
    main()
