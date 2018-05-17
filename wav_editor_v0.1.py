# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 23:33:34 2018

(C) Kirill Mar 2018
"""
import wave, struct


out_dir, input_dir = "output/", "defolt/"

filesname = input("File's name:\n>>").split(".wav")[0]
frame = int(input("Step:\n>>"))

file = input_dir+filesname+".wav"
out_file = out_dir+"out_"+filesname+".wav"

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