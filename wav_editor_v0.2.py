# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:39:53 2018

@author: Glu(K)hov Kirill
"""
import wave, struct
from os import path, mkdir

out_dir, input_dir = "output/", "defolt/"
if not path.exists(out_dir): mkdir(out_dir)
if not path.exists(input_dir): 
    print("Положите .wav файл в", input_dir)
    mkdir(input_dir)

filesname = input("File's name:\n>>").split(".wav")[0]
frame = int(input("Step:\n>>"))

file = input_dir+filesname+".wav"
out_file = out_dir+"out_"+filesname+"_"+str(frame)+".wav"

waveFile = wave.open(file, 'r')
dest = wave.open(out_file, mode="wb")
dest.setparams(waveFile.getparams())

length = waveFile.getnframes()

new_arr = []

print("Wait...")
for i in range(length):
    waveData = waveFile.readframes(1)
    try:
        data = struct.unpack("<2h", waveData)
    except BaseException:
        data = struct.unpack("<h", waveData)
    if i%frame != 0:
        new_arr.append(int(data[0]))
    pass


newframes = struct.pack("<" + str(len(new_arr)) + "h", *new_arr)
dest.writeframes(newframes)
waveFile.close()
dest.close()
print("[V]Done!")