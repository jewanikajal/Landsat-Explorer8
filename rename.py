import os
files = os.listdir("C:/Users/Yash/Desktop/B.E Project/landsatxplore-master")
for src in files:
    dst = src.replace('LC08_L1TP_', '')
    os.rename(src, dst)
for src in files:
    dst = src.replace('_01_T1', '')
    os.rename(src, dst)
