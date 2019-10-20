import numpy as np
import matplotlib.pyplot as plt



def main():
    data = np.loadtxt("Hw11bridge.csv")
    
    datanew = np.abs(np.fft.fft(data))
    
    deltaf = 1/(.025*len(data))
    fnyquist = 1/(2*.025)
    
    fmesh = np.arange(0,fnyquist,deltaf)
    
    plt.plot(fmesh,datanew[:len(datanew)//2],',', label = 'data')
    plt.axvline(x=0.1, label = "Peaks dangerous between red lines", color = "red")
    plt.axvline(x=1, color = "red")
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.title("Plot up to nyquist frequency")
    plt.grid(True)
    plt.show()
    
    
    
    plt.plot(fmesh,datanew[:len(datanew)//2], label = 'data')
    plt.axvline(x=0.1, label = "Peaks dangerous between red lines", color = "red")
    plt.axvline(x=1, color = "red")
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.xlim(0,1.1)
    plt.title("Plot Zoomed into Danger Zone")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    plt.plot(fmesh,datanew[:len(datanew)//2], label = 'data')
    #plt.axvline(x=0.1, label = "Peaks dangerous between red lines", color = "red")
    plt.axvline(x=1, color = "red")
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.xlim(0.7,.9)
    plt.ylim(0,.4)
    plt.title("Plot Zoomed into Major Peak at 0.8")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print("Frequency = 0.8 Hz, Amplitude = 0.33")
    
    plt.plot(fmesh,datanew[:len(datanew)//2], label = 'data')
    #plt.axvline(x=0.1, label = "Peaks dangerous between red lines", color = "red")
    plt.axvline(x=1, color = "red")
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.xlim(.1,.3)
    plt.ylim(0,.4)
    plt.title("Plot Zoomed into Peak at 0.2")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print("Frequency = 0.187 Hz, Amplitude = 0.28")
    print("Appears to be an outlier though")

main()