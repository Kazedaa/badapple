import time
import os

f = open('play.txt', 'r')
frame_raw = f.read()
frame_raw = frame_raw.replace('.', ' ')
f.close()
frames = frame_raw.split('SPLIT')[20:]
init_time = time.time()
while time.time() <= init_time + 218:
	os.system('clear')
	print(frames[int((time.time()-init_time)*10)])
	time.sleep(0.05)